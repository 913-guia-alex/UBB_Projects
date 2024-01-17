public class NBodySimulator
{
    public List<CelestialBody> Bodies { get; set; }

    public NBodySimulator(List<CelestialBody> bodies)
    {
        Bodies = bodies;
    }

    public void SimulateSequential(double timeStep, int numSteps)
    {
        for (int step = 0; step < numSteps; step++)
        {
            CalculateForces();
            UpdatePositionsAndVelocities(timeStep);
        }
    }

        public void SimulateParallelThreads(double timeStep, int numSteps)
    {
        Parallel.For(0, Bodies.Count, i =>
        {
            CalculateForces(i);
            UpdatePositionsAndVelocities(i, timeStep);
        });
    }

    public void SimulateDistributedMPI(double timeStep, int numSteps)
    {
        using (new MPI.Environment(ref MPI.Environment.THREAD_MULTIPLE))
        {
            Intracommunicator world = Communicator.world;

            int numBodiesPerProcess = Bodies.Count / world.Size;

            for (int step = 0; step < numSteps; step++)
            {
                var allBodies = world.Broadcast(Bodies.ToArray(), 0);

                int startIndex = numBodiesPerProcess * world.Rank;
                int endIndex = startIndex + numBodiesPerProcess;

                for (int i = startIndex; i < endIndex; i++)
                {
                    CalculateForces(i, allBodies);
                    UpdatePositionsAndVelocities(i, timeStep, allBodies);
                }

                Bodies = world.Gather(Bodies.ToArray(), 0);
            }
        }
    }

    private void CalculateForces()
    {
        // Implement gravitational force calculations between all pairs of bodies
        for (int i = 0; i < Bodies.Count; i++)
        {
            for (int j = 0; j < Bodies.Count; j++)
            {
                if (i != j)
                {
                    Vector3 force = CalculateGravitationalForce(Bodies[i], Bodies[j]);
                    Bodies[i].Force = Vector3.Add(Bodies[i].Force, force);
                }
            }
        }
    }

    private Vector3 CalculateGravitationalForce(CelestialBody body1, CelestialBody body2)
    {
        // Simplified gravitational force calculation (using Newton's law of gravitation)
        double G = 6.67430e-11; // Gravitational constant
        Vector3 direction = Vector3.Subtract(body2.Position, body1.Position);
        double distance = direction.Length();
        double forceMagnitude = (G * body1.Mass * body2.Mass) / (distance * distance);
        Vector3 force = Vector3.Multiply(Vector3.Normalize(direction), forceMagnitude);
        return force;
    }

    private void UpdatePositionsAndVelocities(double timeStep)
    {
        foreach (var body in Bodies)
        {
            // Update body positions and velocities based on calculated forces
            UpdateBodyPositionAndVelocity(body, timeStep);
        }
    }

    private void UpdateBodyPositionAndVelocity(CelestialBody body, double timeStep)
    {
        // Update position using kinematics equation: position = position + velocity * timeStep
        body.Position = Vector3.Add(body.Position, Vector3.Multiply(body.Velocity, timeStep));

        // Update velocity using Newton's second law: velocity = velocity + acceleration * timeStep
        Vector3 acceleration = Vector3.Divide(body.Force, body.Mass);
        body.Velocity = Vector3.Add(body.Velocity, Vector3.Multiply(acceleration, timeStep));

        // Reset forces for the next iteration
        body.Force = new Vector3(0, 0, 0);
    }
}
