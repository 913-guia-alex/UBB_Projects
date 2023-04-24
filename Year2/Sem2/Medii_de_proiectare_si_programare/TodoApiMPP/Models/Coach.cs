using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace TodoApiMPP.Models;

public class Coach
{
    [Key]
    public int CoachId { get; set; }
    public string? Surname { get; set; }
    public string? Lastname { get; set; }
    public string? Gender { get; set; }
    public int Age { get; set; }
    public int Price { get; set; }
    public ICollection<Clients> Clients { get; set; } = default!;

}