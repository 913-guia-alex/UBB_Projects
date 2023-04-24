using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace TodoApiMPP.Models;

public class Clients
{
    [Key]
    public int CientId { get; set; }
    public string? SurName { get; set; }
    public string? LastName { get; set; }
    public string? Gender { get; set; }
    public int Age { get; set; }
    public string? Experience { get; set; }
    // Foreign key   
    //[Display(Name = "Coach")]
    //public virtual int CoachID { get; set; }  

    [ForeignKey("CoachId")]
    public int CoachId { get; set; } // one coach to many clients

    [ForeignKey("SubscriptionsID")]
    public int SubscriptionID { get; set; }

}