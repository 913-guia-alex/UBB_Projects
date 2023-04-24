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
public class SubscriptionControllerTests
{
    private static List<Subscriptions> GetMockSubscriptions()
    {
        var subscriptions = new List<Subscriptions>
            {
                new Subscriptions { SubscriptionID = 1, SerialNumber = 12345, MadeDate = "10/10/2022", ExpirationDate = "10/10/2023", Entries = 10 },
                new Subscriptions { SubscriptionID = 2, SerialNumber = 23456, MadeDate = "11/11/2022", ExpirationDate = "11/11/2023", Entries = 5 },
                new Subscriptions { SubscriptionID = 3, SerialNumber = 34567, MadeDate = "12/12/2022", ExpirationDate = "12/12/2023", Entries = 20 }
            };
        return subscriptions;
    }

    private static List<Clients> GetMockClients()
    {
        var clients = new List<Clients>
            {
                new Clients { CientId = 1, SurName = "John", Age = 25, SubscriptionID = 1 },
                new Clients { CientId = 2, SurName = "Jane", Age = 30, SubscriptionID = 1 },
                new Clients { CientId = 3, SurName = "Bob", Age = 20, SubscriptionID = 2 },
                new Clients { CientId = 4, SurName = "Alice", Age = 35, SubscriptionID = 3 }
            };
        return clients;
    }

    private static DataBaseContext GetMockContext()
    {
        var subscriptions = GetMockSubscriptions();
        var clients = GetMockClients();

        var options = new DbContextOptionsBuilder<DataBaseContext>()
            .UseInMemoryDatabase(databaseName: "MockDB")
            .Options;

        var context = new DataBaseContext(options);
        context.Subscriptions.AddRange(subscriptions);
        context.Clients.AddRange(clients);
        context.SaveChanges();

        return context;
    }
    [Fact]
    public async Task GetSubscriptionsByAge_ReturnsSubscriptionsWithClientsAboveAge()
    {
        // Arrange
        var mockContext = GetMockContext();
        var mapperConfig = new MapperConfiguration(cfg =>
        {
            cfg.AddProfile(new SubscriptionsMappings());
        });
        var mapper = mapperConfig.CreateMapper();
        var controller = new SubscriptionsController(mockContext, mapper);
        var expectedSubscriptions = await mockContext.Subscriptions
            .Where(s => mockContext.Clients.Any(c => c.SubscriptionID == s.SubscriptionID && c.Age > 25))
            .ToListAsync();

        // Act
        var actionResult = await controller.GetSubscriptionsByAge(25);
        var result = actionResult.Result as OkObjectResult;
        var actualSubscriptions = result.Value as List<SubscriptionsDTO>;

        // Assert
        Assert.IsNotNull(result);
        Assert.Equals(200, result.StatusCode);
        Assert.Equals(expectedSubscriptions.Select(s => s.SubscriptionID).ToList(), actualSubscriptions.Select(s => s.SubscriptionID).ToList());
    }

}

