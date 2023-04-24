using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace TodoApiMPP.Migrations
{
    /// <inheritdoc />
    public partial class Migrationsss : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Coaches",
                columns: table => new
                {
                    CoachId = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Surname = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Lastname = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Gender = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Age = table.Column<int>(type: "int", nullable: false),
                    Price = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Coaches", x => x.CoachId);
                });

            migrationBuilder.CreateTable(
                name: "Products",
                columns: table => new
                {
                    ProductId = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Name = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Price = table.Column<int>(type: "int", nullable: false),
                    Type = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    MadeDate = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    ExpirationDate = table.Column<string>(type: "nvarchar(max)", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Products", x => x.ProductId);
                });

            migrationBuilder.CreateTable(
                name: "Shop",
                columns: table => new
                {
                    ShopID = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Name = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    StreetName = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    StreetNumber = table.Column<int>(type: "int", nullable: false),
                    AverageCustomers = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Shop", x => x.ShopID);
                });

            migrationBuilder.CreateTable(
                name: "Subscriptions",
                columns: table => new
                {
                    SubscriptionID = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    SerialNumber = table.Column<int>(type: "int", nullable: false),
                    MadeDate = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    ExpirationDate = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Entries = table.Column<int>(type: "int", nullable: false),
                    ClientId = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Subscriptions", x => x.SubscriptionID);
                });

            migrationBuilder.CreateTable(
                name: "ProductShop",
                columns: table => new
                {
                    ShopID = table.Column<int>(type: "int", nullable: false),
                    ProductId = table.Column<int>(type: "int", nullable: false),
                    ProductShopId = table.Column<int>(type: "int", nullable: false),
                    SerialNumber = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_ProductShop", x => new { x.ProductId, x.ShopID });
                    table.ForeignKey(
                        name: "FK_ProductShop_Products_ProductId",
                        column: x => x.ProductId,
                        principalTable: "Products",
                        principalColumn: "ProductId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_ProductShop_Shop_ShopID",
                        column: x => x.ShopID,
                        principalTable: "Shop",
                        principalColumn: "ShopID",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "ProductsShop",
                columns: table => new
                {
                    ProductsProductId = table.Column<int>(type: "int", nullable: false),
                    ShopsShopID = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_ProductsShop", x => new { x.ProductsProductId, x.ShopsShopID });
                    table.ForeignKey(
                        name: "FK_ProductsShop_Products_ProductsProductId",
                        column: x => x.ProductsProductId,
                        principalTable: "Products",
                        principalColumn: "ProductId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_ProductsShop_Shop_ShopsShopID",
                        column: x => x.ShopsShopID,
                        principalTable: "Shop",
                        principalColumn: "ShopID",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "Clients",
                columns: table => new
                {
                    CientId = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    SurName = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    LastName = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Gender = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Age = table.Column<int>(type: "int", nullable: false),
                    Experience = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    CoachId = table.Column<int>(type: "int", nullable: false),
                    SubscriptionID = table.Column<int>(type: "int", nullable: false),
                    SubscriptionsSubscriptionID = table.Column<int>(type: "int", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Clients", x => x.CientId);
                    table.ForeignKey(
                        name: "FK_Clients_Coaches_CoachId",
                        column: x => x.CoachId,
                        principalTable: "Coaches",
                        principalColumn: "CoachId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_Clients_Subscriptions_SubscriptionsSubscriptionID",
                        column: x => x.SubscriptionsSubscriptionID,
                        principalTable: "Subscriptions",
                        principalColumn: "SubscriptionID");
                });

            migrationBuilder.CreateIndex(
                name: "IX_Clients_CoachId",
                table: "Clients",
                column: "CoachId");

            migrationBuilder.CreateIndex(
                name: "IX_Clients_SubscriptionsSubscriptionID",
                table: "Clients",
                column: "SubscriptionsSubscriptionID");

            migrationBuilder.CreateIndex(
                name: "IX_ProductShop_ShopID",
                table: "ProductShop",
                column: "ShopID");

            migrationBuilder.CreateIndex(
                name: "IX_ProductsShop_ShopsShopID",
                table: "ProductsShop",
                column: "ShopsShopID");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Clients");

            migrationBuilder.DropTable(
                name: "ProductShop");

            migrationBuilder.DropTable(
                name: "ProductsShop");

            migrationBuilder.DropTable(
                name: "Coaches");

            migrationBuilder.DropTable(
                name: "Subscriptions");

            migrationBuilder.DropTable(
                name: "Products");

            migrationBuilder.DropTable(
                name: "Shop");
        }
    }
}
