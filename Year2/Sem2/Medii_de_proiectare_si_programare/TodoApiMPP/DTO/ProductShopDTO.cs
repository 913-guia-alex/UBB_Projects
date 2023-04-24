using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace TodoApiMPP.Models;

public class ProductShopDTO
{
    public int SerialNumber { get; set; }
    public int ShopID { get; set; } // one coach to many clients
    public int ProductId { get; set; } // one coach to many clients

}