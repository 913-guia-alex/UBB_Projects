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
    public class SubscriptionsController : ControllerBase
    {
        private readonly DataBaseContext _context;
        private readonly IMapper _mapper;

        private readonly Validations _validator = new Validations();



        public SubscriptionsController(DataBaseContext context, IMapper mappper)
        {
            _context = context;
            _mapper = mappper;

        }

        // GET: api/Subscriptions
        [HttpGet]
        public async Task<ActionResult<IEnumerable<SubscriptionsDTO>>> GetSubscriptions()
        {
            if (_context.Subscriptions == null)
            {
                return NotFound();
            }
            var subscriptions = await _context.Subscriptions
                 .Select(s => new SubscriptionsDTO
                 {
                     SubscriptionID = s.SubscriptionID,
                     SerialNumber = s.SerialNumber,
                     MadeDate = s.MadeDate,
                     ExpirationDate = s.ExpirationDate,
                     Entries = s.Entries,
                     ClientId = s.ClientId,
                 })
               .ToListAsync();
            if (subscriptions == null)
            {
                return NotFound();
            }
            return subscriptions;
        }
        // GET: api/Subscriptions/5
        [HttpGet("{id}")]
        public ActionResult<SubscriptionsDTO> Get(int id)
        {
            var subscription = _context.Subscriptions
                .Include(s => s.Clients)
                .SingleOrDefault(s => s.SubscriptionID == id);

            if (subscription == null)
            {
                return NotFound();
            }

            var subscriptionDto = _mapper.Map<SubscriptionsDTO>(subscription);

            return Ok(subscriptionDto);
        }
        // PUT: api/Subscriptions/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutSubscriptions(int id, Subscriptions subscriptions)
        {
            if (id != subscriptions.SubscriptionID)
            {
                return BadRequest();
            }

            _context.Entry(subscriptions).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!SubscriptionsExists(id))
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

        // POST: api/Subscriptions
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Subscriptions>> PostSubscriptions(Subscriptions subscriptions)
        {
            if (_context.Subscriptions == null)
            {
                return Problem("Entity set 'DataBaseContext.Subscriptions'  is null.");
            }

            if (!_validator.ValidationSubscription(subscriptions))
            {
                return BadRequest();
            }

            _context.Subscriptions.Add(subscriptions);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetSubscriptions", new { id = subscriptions.SubscriptionID }, subscriptions);
        }

        // DELETE: api/Subscriptions/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteSubscriptions(int id)
        {
            if (_context.Subscriptions == null)
            {
                return NotFound();
            }
            var subscriptions = await _context.Subscriptions.FindAsync(id);
            if (subscriptions == null)
            {
                return NotFound();
            }

            _context.Subscriptions.Remove(subscriptions);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        [HttpGet("age/{age}")]
        public async Task<ActionResult<IEnumerable<SubscriptionsDTO>>> GetSubscriptionsByAge(int age)
        {
            var clients = await _context.Clients.Where(c => c.Age > age).ToListAsync();

            var subscriptions = new List<SubscriptionsDTO>();
            foreach (var client in clients)
            {
                var subscription = await _context.Subscriptions.FindAsync(client.SubscriptionID);
                if (subscription != null)
                {
                    var subscriptionDTO = _mapper.Map<SubscriptionsDTO>(subscription);
                    subscriptionDTO.ClientId = client.CientId;
                    subscriptions.Add(subscriptionDTO);
                }
            }

            return subscriptions;
        }

       
        private bool SubscriptionsExists(int id)
        {
            return (_context.Subscriptions?.Any(e => e.SubscriptionID == id)).GetValueOrDefault();
        }
    }
}
