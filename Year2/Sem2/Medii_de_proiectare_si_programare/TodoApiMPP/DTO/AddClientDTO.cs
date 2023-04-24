using System.Runtime.CompilerServices;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;
using TodoApiMPP.Models;

namespace TodoApiMPP.DTO
{
    public class AddClientDTO
    {
        [Required]
        public string Surname { get; set; } = string.Empty;
        [Required]
        public string Lastname { get; set; } = string.Empty;
        [Required]
        public string Gender { get; set; } = string.Empty;
        [Required]
        public int Age { get; set; }
        [Required]
        public string Experience { get; set; } = string.Empty;
        public int CoachId { get; set; }
        public int SubscriptionID { get; set; }
    }
}