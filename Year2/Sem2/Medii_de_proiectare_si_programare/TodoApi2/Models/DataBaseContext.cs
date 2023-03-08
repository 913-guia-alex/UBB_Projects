using Microsoft.EntityFrameworkCore;

namespace TodoApi2.Models;

public class DataBaseContext : DbContext
{
    public DataBaseContext(DbContextOptions<DataBaseContext> options)
        : base(options)
    {
    }

    public DbSet<Coach> Coaches { get; set; } = null!;
}