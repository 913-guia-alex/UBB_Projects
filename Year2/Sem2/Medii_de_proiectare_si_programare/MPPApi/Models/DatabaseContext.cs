using Microsoft.EntityFrameworkCore;

namespace MPPApi.Models;

public class DatabaseContext : DbContext
{
    public DatabaseContext(DbContextOptions<DatabaseContext> options)
        : base(options)
    {
    }
    public DbSet<Coach> Coaches { get; set; } = null!;
}