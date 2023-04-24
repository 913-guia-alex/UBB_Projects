using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;

namespace TodoApiMPP.Models;

public class ShopDTO
{
    public string? Name { get; set; }
    public string? StreetName { get; set; }
    public int StreetNumber { get; set; }
    public int AverageCustomers { get; set; }


}