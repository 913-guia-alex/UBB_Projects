using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TodoApiMPP.Models;

namespace TodoApiMPP.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ShopController : ControllerBase
    {
        private readonly DataBaseContext _context;

        public ShopController(DataBaseContext context)
        {
            _context = context;
        }

        // GET: api/Shop
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Shop>>> GetShop()
        {
          if (_context.Shop == null)
          {
              return NotFound();
          }
            return await _context.Shop.ToListAsync();
        }

        // GET: api/Shop/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Shop>> GetShop(int id)
        {
          if (_context.Shop == null)
          {
              return NotFound();
          }
            var shop = await _context.Shop.FindAsync(id);

            if (shop == null)
            {
                return NotFound();
            }

            return shop;
        }

        // PUT: api/Shop/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutShop(int id, Shop shop)
        {
            if (id != shop.ShopID)
            {
                return BadRequest();
            }

            _context.Entry(shop).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!ShopExists(id))
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

        // POST: api/Shop
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Shop>> PostShop(Shop shop)
        {
          if (_context.Shop == null)
          {
              return Problem("Entity set 'DataBaseContext.Shop'  is null.");
          }
            _context.Shop.Add(shop);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetShop", new { id = shop.ShopID }, shop);
        }

        // DELETE: api/Shop/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteShop(int id)
        {
            if (_context.Shop == null)
            {
                return NotFound();
            }
            var shop = await _context.Shop.FindAsync(id);
            if (shop == null)
            {
                return NotFound();
            }

            _context.Shop.Remove(shop);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool ShopExists(int id)
        {
            return (_context.Shop?.Any(e => e.ShopID == id)).GetValueOrDefault();
        }
    }
}
