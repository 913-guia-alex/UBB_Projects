using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;
using TodoApiMPP.Models;

namespace TodoApiMPP.DTO;

public class ClientDTO
{
    public int ClientId { get; set; }
    public string SurName { get; set; } = string.Empty;
    public string LastName { get; set; } = string.Empty;
    public string Gender { get; set; } = string.Empty;
    public int Age { get; set; }
    public string Experience { get; set; } = string.Empty;
    public int CoachId { get; set; }
    public int SubscriptionID { get; set; }

    public static ClientDTO FromClient(Clients client)
    {
        return new ClientDTO
        {
            ClientId = client.CientId,
            SurName = client.SurName!,
            LastName = client.LastName!,
            Gender = client.Gender!,
            Age = client.Age,
            Experience = client.Experience!,
            CoachId = client.CoachId,
            SubscriptionID = client.SubscriptionID
        };
    }
}
