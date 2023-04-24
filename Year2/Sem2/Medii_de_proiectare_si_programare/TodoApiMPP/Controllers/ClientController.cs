using System.ComponentModel.DataAnnotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AutoMapper;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;
namespace TodoApiMPP.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClientController : ControllerBase
    {
        private readonly DataBaseContext _context;
        private readonly IMapper _mapper;
        private readonly Validations _validator = new Validations();


        public ClientController(DataBaseContext context, IMapper mappper)
        {
            _context = context;
            _mapper = mappper;

        }

        // GET: api/Client
        [HttpGet]
        public async Task<ActionResult<IEnumerable<ClientDTO>>> GetClients()
        {
            if (_context.Clients == null)
            {
                return NotFound();
            }
            var clients = await _context.Clients
                 .Select(c => new ClientDTO
                 {
                     ClientId = c.CientId,
                     SurName = c.SurName!,
                     LastName = c.LastName!,
                     Gender = c.Gender!,
                     Age = c.Age,
                     Experience = c.Experience!,
                     CoachId = c.CoachId,
                     SubscriptionID = c.SubscriptionID,
                 })
               .ToListAsync();
            if (clients == null)
            {
                return NotFound();
            }
            return clients;
        }

        // GET: api/Client/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Clients>> GetClientsById(int id)
        {
            if (_context.Clients == null)
            {
                return NotFound();
            }
            var clients = await _context.Clients.FindAsync(id);

            if (clients == null)
            {
                return NotFound();
            }

            var coach = await _context.Coaches.FindAsync(clients.CoachId);
            var clientDTO = ClientDTO.FromClient(clients);
            clientDTO.CoachId = coach!.CoachId;

            return clients;
        }

        // PUT: api/Client/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutClients(int id, Clients clients)
        {
            if (id != clients.CientId)
            {
                return BadRequest();
            }

            _context.Entry(clients).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!ClientsExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Client
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<IActionResult> PostClients(AddClientDTO addClientDTO)
        {
            var newClient = _mapper.Map<Clients>(addClientDTO);

            if (_context.Clients == null)
            {
                return Problem("Entity set 'DataBaseContext.Clients'  is null.");
            }

            if (!_validator.ValidationClient(newClient))
            {
                return BadRequest();
            }

            _context.Clients.Add(newClient);
            await _context.SaveChangesAsync();

            return Created(nameof(GetClientsById), _mapper.Map<ClientDTO>(newClient));
        }

        // DELETE: api/Client/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteClients(int id)
        {
            if (_context.Clients == null)
            {
                return NotFound();
            }
            var clients = await _context.Clients.FindAsync(id);
            if (clients == null)
            {
                return NotFound();
            }

            _context.Clients.Remove(clients);
            await _context.SaveChangesAsync();

            return NoContent();
        }


        [HttpPost("{id}/clients")]
        public async Task<IActionResult> PostClients(int id, [FromBody] List<AddClientDTO> addClientsDTO)
        {
            var coach = await _context.Coaches.FindAsync(id);
            if (coach == null)
            {
                return NotFound();
            }

            foreach (var addClientDTO in addClientsDTO)
            {
                var newClient = new Clients
                {
                    SurName = addClientDTO.Surname,
                    LastName = addClientDTO.Lastname,
                    Gender = addClientDTO.Gender,
                    Age = addClientDTO.Age,
                    Experience = addClientDTO.Experience,
                    CoachId = id,
                    SubscriptionID = addClientDTO.SubscriptionID
                };

                if (!IsValid(newClient))
                {
                    return BadRequest();
                }

                _context.Clients.Add(newClient);
            }

            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetClientsByCoach), new { id }, addClientsDTO);
        }

        [HttpGet("{id}/clients")]
        public async Task<ActionResult<IEnumerable<ClientDTO>>> GetClientsByCoach(int id)
        {
            var coach = await _context.Coaches.FindAsync(id);
            if (coach == null)
            {
                return NotFound();
            }

            var clients = await _context.Clients
                .Where(c => c.CoachId == id)
                .Select(c => new ClientDTO
                {
                    ClientId = c.CientId,
                    SurName = c.SurName!,
                    LastName = c.LastName!,
                    Gender = c.Gender!,
                    Age = c.Age,
                    Experience = c.Experience!,
                    CoachId = c.CoachId,
                    SubscriptionID = c.SubscriptionID,
                })
                .ToListAsync();

            return clients;
        }

        private bool IsValid(Clients client)
        {
            // Add your validation logic here
            return true;
        }

        private bool ClientsExists(int id)
        {
            return (_context.Clients?.Any(e => e.CientId == id)).GetValueOrDefault();
        }
    }
}
