using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace TodoApiMPP.Models;

public class ProductsDTO
{
    public string? Name { get; set; }
    public int Price { get; set; }
    public string? Type { get; set; }
    public string? MadeDate { get; set; }
    public string? ExpirationDate { get; set; }

}