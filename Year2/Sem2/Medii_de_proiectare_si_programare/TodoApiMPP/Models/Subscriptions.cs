
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace TodoApiMPP.Models;


public class Subscriptions
{
    [Key]
    public int SubscriptionID { get; set; }
    public int SerialNumber { get; set; }
    public string? MadeDate { get; set; }
    public string? ExpirationDate { get; set; }
    public int Entries { get; set; }

    [ForeignKey("ClientId")]
    public int ClientId { get; set; } //one client to one subsctiptions
    public ICollection<Clients> Clients { get; set; } = default!;

}