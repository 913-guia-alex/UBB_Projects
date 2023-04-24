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
    public class CoachController : ControllerBase
    {
        private readonly DataBaseContext _context;
        private readonly IMapper _mapper;

        private readonly Validations _validator = new Validations();


        public CoachController(DataBaseContext context, IMapper mappper)
        {
            _context = context;
            _mapper = mappper;
        }

        // GET: api/Coach
        [HttpGet]
        public async Task<ActionResult<IEnumerable<CoachDTO>>> GetCoaches()
        {
            var coaches = await _context.Coaches
                .Include(c => c.Clients)
                .ToListAsync();

            var coachesDTO = coaches.Select(CoachDTO.FromCoach);

            return Ok(coachesDTO);
        }

        [HttpGet("clients/{coachId}")]
        public async Task<ActionResult<CoachDTO>> GetCoachById(int id)
        {
            var coach = await _context.Coaches
                .Include(c => c.Clients)
                .FirstOrDefaultAsync(c => c.CoachId == id);

            if (coach == null)
            {
                return NotFound();
            }

            var coachDto = CoachDTO.FromCoach(coach);

            return coachDto;
        }

        // PUT: api/Coach/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutCoach(long id, Coach coach)
        {
            if (id != coach.CoachId)
            {
                return BadRequest();
            }

            _context.Entry(coach).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!CoachExists(id))
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

        // POST: api/Coach
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<IActionResult> PostCoaches(AddCoachDTO addCoachDTO)
        {
            var newCoach = _mapper.Map<Coach>(addCoachDTO);

            if (_context.Coaches == null)
            {
                return Problem("Entity set 'DataBaseContext.Coach'  is null.");
            }

            if (!_validator.ValidationCoach(newCoach))
            {
                return BadRequest();
            }
            _context.Coaches.Add(newCoach);
            await _context.SaveChangesAsync();

            return Created(nameof(GetCoachById), _mapper.Map<CoachDTO>(newCoach));
        }

        // DELETE: api/Coach/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteCoach(long id)
        {
            if (_context.Coaches == null)
            {
                return NotFound();
            }
            var coach = await _context.Coaches.FindAsync(id);
            if (coach == null)
            {
                return NotFound();
            }

            _context.Coaches.Remove(coach);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        // GET: api/Coach/filter/5
        [HttpGet("filter/{Price}")]
        public async Task<ActionResult<IEnumerable<CoachDTO>>> GetCoachesByPrice(long Price)
        {
            if (_context.Coaches == null)
            {
                return NotFound();
            }

            var coaches = await _context.Coaches.Where(x => x.Price > Price)
                                                .ToListAsync();

            if (coaches == null)
            {
                return NotFound();
            }

            return coaches.Select(c => CoachDTO.FromCoach(c)).ToList();
        }

        // GET: api/Coach
        [HttpGet("coach/filter/{Age}")]
        public async Task<ActionResult<IEnumerable<Coach>>> GetCoachesByAge()
        {
            if (_context.Coaches == null)
            {
                return NotFound();
            }

            var coachesOrderByAge = await _context.Coaches
                .Include(c => c.Clients)
                .Select(c => new
                {
                    Coach = c,
                    AvgClientAge = c.Clients.Average(cl => cl.Age)
                })
                .OrderByDescending(c => c.AvgClientAge)
                .Select(c => c.Coach)
                .ToListAsync();

            if (coachesOrderByAge == null)
            {
                return NotFound();
            }

            return coachesOrderByAge;
        }

        private bool CoachExists(long id)
        {
            return (_context.Coaches?.Any(e => e.CoachId == id)).GetValueOrDefault();
        }
    }
}
