using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;
using TodoApiMPP.Models;


namespace TodoApiMPP.DTO
{
    public class CoachDTO
    {
        public int CoachId { get; set; }
        public string Name { get; set; } = string.Empty;
        public string Surname { get; set; } = string.Empty;
        public string Gender { get; set; } = string.Empty;
        public int Age { get; set; }
        public int Price { get; set; }
        public List<ClientDTO> Clients { get; set; } = new List<ClientDTO>();

        public static CoachDTO FromCoach(Coach coach)
        {
            return new CoachDTO
            {
                CoachId = coach.CoachId,
                Surname = coach.Surname!,
                Name = coach.Lastname!,
                Gender = coach.Gender!,
                Age = coach.Age,
                Price = coach.Price,
                Clients = coach.Clients?.Select(ClientDTO.FromClient).ToList() ?? new List<ClientDTO>()
            };
        }
    }
}