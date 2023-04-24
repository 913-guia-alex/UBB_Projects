using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;
using TodoApiMPP.Models;

namespace TodoApiMPP.Models;

public class DataBaseContext : DbContext
{
    public DataBaseContext(DbContextOptions<DataBaseContext> options)
        : base(options)
    {
    }

    public DbSet<Coach> Coaches { get; set; } = default!;

    public DbSet<Products> Products { get; set; } = default!;

    public DbSet<Shop> Shop { get; set; } = default!;

    public DbSet<Clients> Clients { get; set; } = default!;

    public DbSet<Subscriptions> Subscriptions { get; set; } = default!;

    public DbSet<ProductShop> ProductShop { get; set; } = default!;

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        //Many to many for Certifications
        modelBuilder.Entity<ProductShop>()
            .HasKey(c => new { c.ProductId, c.ShopID });
        modelBuilder.Entity<ProductShop>()
            .HasOne(c => c.Products)
            .WithMany(c => c.ProductShops)
            .HasForeignKey(c => c.ProductId);

        modelBuilder.Entity<ProductShop>()
            .HasOne(c => c.Shops)
            .WithMany(c => c.ProductShops)
            .HasForeignKey(c => c.ShopID);
        /*
        //One to many for Album-RecordLabel
        modelBuilder.Entity<Album>()
            .HasOne(a => a.RecordLabel)
            .WithMany(r => r.Albums)
            .HasForeignKey(a => a.RecordLabelId);

        //One to many for Album-Artist
        modelBuilder.Entity<Album>()
            .HasOne(a => a.Artist)
            .WithMany(r => r.Albums)
            .HasForeignKey(a => a.ArtistId);*/
    }

}