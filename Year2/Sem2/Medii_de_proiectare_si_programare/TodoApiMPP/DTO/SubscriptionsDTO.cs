using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AutoMapper;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;


namespace TodoApiMPP.Models;


public class SubscriptionsDTO
{
    public int SubscriptionID { get; set; }
    public int SerialNumber { get; set; }
    public string? MadeDate { get; set; }
    public string? ExpirationDate { get; set; }
    public int Entries { get; set; }
    public int ClientId { get; set; } //one client to one subsctiptions
    //public Clients Clients { get; set; } = default!;

}