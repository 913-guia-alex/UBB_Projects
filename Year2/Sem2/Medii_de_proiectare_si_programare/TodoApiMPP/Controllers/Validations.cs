using System.Reflection.PortableExecutable;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.FileProviders;
using System.Text.RegularExpressions;
using System;

namespace TodoApiMPP.Controllers
{
    public class Validations
    {
        public bool ValidationClient(Clients clients)
        {
            if (clients.Age <= 0 && clients.Age >= 100)
            {
                return false;
            }

            if (clients.Experience != "Beginner" && clients.Experience != "Intermediate" && clients.Experience != "Advanced")
            {
                return false;
            }

            if (!Regex.IsMatch(clients.SurName, @"^[a-zA-Z\-]+$"))
            {
                return false;
            }

            if (!Regex.IsMatch(clients.LastName, @"^[a-zA-Z\-]+$"))
            {
                return false;
            }

            return true;
        }
        public bool ValidationCoach(Coach coach)
        {
            if (coach.Age <= 0 && coach.Age >= 100)
            {
                return false;
            }

            if (coach.Price <= 0 && coach.Price >= 10000)
            {
                return false;
            }

            if (!Regex.IsMatch(coach.Lastname, @"^[a-zA-Z\-]+$"))
            {
                return false;
            }

            if (!Regex.IsMatch(coach.Surname, @"^[a-zA-Z\-]+$"))
            {
                return false;
            }

            return true;
        }
        public bool ValidationSubscription(Subscriptions subscriptions)
        {
            if (subscriptions.SerialNumber <= 10000 && subscriptions.SerialNumber >= 1000000)
            {
                return false;
            }

            if (subscriptions.Entries < 0)
            {
                return false;
            }

            return true;
        }

    }
}