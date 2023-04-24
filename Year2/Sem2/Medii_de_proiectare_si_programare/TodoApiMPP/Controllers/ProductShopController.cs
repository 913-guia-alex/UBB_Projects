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
    public class ProductShopController : ControllerBase
    {
        private readonly DataBaseContext _context;

        public ProductShopController(DataBaseContext context)
        {
            _context = context;
        }

        // GET: api/ProductShop
        [HttpGet]
        public async Task<ActionResult<IEnumerable<ProductShop>>> GetProductShop()
        {
            if (_context.ProductShop == null)
            {
                return NotFound();
            }
            return await _context.ProductShop.ToListAsync();
        }

        // GET: api/ProductShop/5
        [HttpGet("{id}")]
        public async Task<ActionResult<ProductShop>> GetProductShop(int id)
        {
            if (_context.ProductShop == null)
            {
                return NotFound();
            }
            var productShop = await _context.ProductShop.FindAsync(id);

            if (productShop == null)
            {
                return NotFound();
            }

            return productShop;
        }

        // PUT: api/ProductShop/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutProductShop(int id, ProductShop productShop)
        {
            if (id != productShop.ProductShopId)
            {
                return BadRequest();
            }

            _context.Entry(productShop).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!ProductShopExists(id))
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

        // POST: api/ProductShop
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<ProductShop>> PostProductShop(ProductShop productShop)
        {
            if (_context.ProductShop == null)
            {
                return Problem("Entity set 'DataBaseContext.ProductShop'  is null.");
            }
            _context.ProductShop.Add(productShop);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetProductShop", new { id = productShop.ProductShopId }, productShop);
        }

        // DELETE: api/ProductShop/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteProductShop(int id)
        {
            if (_context.ProductShop == null)
            {
                return NotFound();
            }
            var productShop = await _context.ProductShop.FindAsync(id);
            if (productShop == null)
            {
                return NotFound();
            }

            _context.ProductShop.Remove(productShop);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool ProductShopExists(int id)
        {
            return (_context.ProductShop?.Any(e => e.ProductShopId == id)).GetValueOrDefault();
        }
    }
}
