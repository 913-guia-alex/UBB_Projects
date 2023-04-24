using Microsoft.EntityFrameworkCore;
using TodoApiMPP.Mappings;
using TodoApiMPP.Models;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<DataBaseContext>(opt => opt.UseSqlServer(builder.Configuration.GetConnectionString("GymDataBase")));

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.ConfigureSwaggerGen(setup =>
{
    setup.SwaggerDoc("v1", new Microsoft.OpenApi.Models.OpenApiInfo
    {
        Title = "TodoApiMPP",
        Version = "v1"
    });
});

builder.Services.AddAutoMapper(typeof(CoachMappings));

builder.Services.AddAutoMapper(typeof(ClientMappings));

builder.Services.AddAutoMapper(typeof(ProductsMappings));


var app = builder.Build();

app.UseSwagger();
app.UseSwaggerUI();


app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();