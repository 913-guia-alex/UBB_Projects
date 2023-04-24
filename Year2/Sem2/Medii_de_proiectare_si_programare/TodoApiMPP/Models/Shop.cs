using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;

namespace TodoApiMPP.Models;

public class Shop
{
    [Key]
    public int ShopID { get; set; }
    public string? Name { get; set; }
    public string? StreetName { get; set; }
    public int StreetNumber { get; set; }
    public int AverageCustomers { get; set; }

    public virtual ICollection<Products> Products { get; set; } = null!;
    public virtual ICollection<ProductShop> ProductShops { get; set; } = null!;


}