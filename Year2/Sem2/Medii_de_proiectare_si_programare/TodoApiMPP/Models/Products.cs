using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace TodoApiMPP.Models;

public class Products
{
    [Key]
    public int ProductId { get; set; }
    public string? Name { get; set; }
    public int Price { get; set; }
    public string? Type { get; set; }
    public string? MadeDate { get; set; }
    public string? ExpirationDate { get; set; }

    public virtual ICollection<Shop> Shops { get; set; } = null!;
    public virtual ICollection<ProductShop> ProductShops { get; set; } = null!;

}