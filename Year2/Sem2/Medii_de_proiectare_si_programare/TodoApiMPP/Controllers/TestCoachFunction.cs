using System.ComponentModel;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Moq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using TodoApiMPP.Controllers;
using TodoApiMPP.Mappings;
using TodoApiMPP.DTO;
using TodoApiMPP.Models;
using Xunit;
namespace TodoApiMPP.Tests;
using AutoMapper;
using Microsoft.VisualStudio.TestTools.UnitTesting;


[TestClass]
public class CoachControllerTests
{
    private static List<Coach> GetMockCoaches()
    {
        var coaches = new List<Coach>
            {
                new Coach { CoachId = 1, Surname = "John", Age = 25 },
                new Coach { CoachId = 2, Surname = "Jane", Age = 30 },
                new Coach { CoachId = 3, Surname = "Bob", Age = 20 },
                new Coach { CoachId = 4, Surname = "Alice", Age = 35 }
            };
        return coaches;
    }

    private static List<Clients> GetMockClients()
    {
        var clients = new List<Clients>
            {
                new Clients { CientId = 1, SurName = "John", Age = 25, CoachId = 1 },
                new Clients { CientId = 2, SurName = "Jane", Age = 30, CoachId = 1 },
                new Clients { CientId = 3, SurName = "Bob", Age = 20, CoachId = 2 },
                new Clients { CientId = 4, SurName = "Alice", Age = 35, CoachId = 3 }
            };
        return clients;
    }

    private static DataBaseContext GetMockContext()
    {
        var coaches = GetMockCoaches();
        var clients = GetMockClients();

        var options = new DbContextOptionsBuilder<DataBaseContext>()
            .UseInMemoryDatabase(databaseName: "MockDB")
            .Options;

        var context = new DataBaseContext(options);
        context.Coaches.AddRange(coaches);
        context.Clients.AddRange(clients);
        context.SaveChanges();

        return context;
    }

    [TestMethod]
    public async Task GetCoachesByAge_ReturnsCoachesWithClientsAboveAge()
    {
        // Arrange
        var mockContext = GetMockContext();
        var mapperConfig = new MapperConfiguration(cfg =>
        {
            cfg.AddProfile(new CoachMappings());
        });
        var mapper = mapperConfig.CreateMapper();
        var controller = new CoachController(mockContext, mapper);
        var expectedCoaches = await mockContext.Coaches
            .Where(c => mockContext.Clients.Any(cl => cl.CoachId == c.CoachId && cl.Age > 25))
            .ToListAsync();

        // Act
        var actionResult = await controller.GetCoachesByPrice(25);
        var result = actionResult.Result as OkObjectResult;
        var actualCoaches = result.Value as List<Coach>;

        // Assert
        Assert.IsNotNull(result);
        Assert.AreEqual(200, result.StatusCode);
        CollectionAssert.AreEqual(expectedCoaches.Select(c => c.CoachId).ToList(), actualCoaches.Select(c => c.CoachId).ToList());
    }

}







