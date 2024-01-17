using System;
using System.Collections.Generic;
using MPI;

class Program
{
    static void Main(string[] args)
    {
        MPI.Environment.Run(ref args, communicator =>
        {
            // Create a list of celestial bodies
            List<CelestialBody> bodies = InitializeBodies();

            // Create an NBodySimulator instance for sequential simulation
            NBodySimulator sequentialSimulator = new NBodySimulator(new List<CelestialBody>(bodies));

            Console.WriteLine("Sequential Simulation:");
            SimulateAndPrint(sequentialSimulator, 0.1, 100);

            // Create an NBodySimulator instance for parallel simulation with threads
            NBodySimulator parallelThreadsSimulator = new NBodySimulator(new List<CelestialBody>(bodies));

            Console.WriteLine("\nParallel Simulation with Threads:");
            SimulateAndPrint(parallelThreadsSimulator.SimulateParallelThreads, 0.1, 100);

            // Create an NBodySimulator instance for distributed simulation with MPI
            NBodySimulator distributedMPISimulator = new NBodySimulator(new List<CelestialBody>(bodies));

            Console.WriteLine("\nDistributed Simulation with MPI:");
            SimulateAndPrint(distributedMPISimulator.SimulateDistributedMPI, 0.1, 100);

        });

        Console.ReadLine();
    }

    static List<CelestialBody> InitializeBodies()
    {
        // Create and return a list of celestial bodies with initial properties
        // Add your initialization logic here
        List<CelestialBody> bodies = new List<CelestialBody>
        {
            // Example initialization for three bodies
            new CelestialBody { Mass = 1.0, Position = new Vector3(0.0, 0.0, 0.0), Velocity = new Vector3(0.0, 0.0, 0.0) },
            new CelestialBody { Mass = 1.0, Position = new Vector3(1.0, 0.0, 0.0), Velocity = new Vector3(0.0, 1.0, 0.0) },
            new CelestialBody { Mass = 1.0, Position = new Vector3(0.0, 1.0, 0.0), Velocity = new Vector3(1.0, 0.0, 0.0) }
        };

        return bodies;
    }

    static void SimulateAndPrint(Action<double, int> simulationMethod, double timeStep, int numSteps)
    {
        // Measure time taken for the simulation
        var stopwatch = System.Diagnostics.Stopwatch.StartNew();

        // Perform the simulation
        simulationMethod.Invoke(timeStep, numSteps);

        // Stop the stopwatch and print the elapsed time
        stopwatch.Stop();
        Console.WriteLine($"Simulation completed in {stopwatch.ElapsedMilliseconds} milliseconds.");
    }
}
