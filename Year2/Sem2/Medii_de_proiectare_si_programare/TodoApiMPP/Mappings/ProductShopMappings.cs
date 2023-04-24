using AutoMapper;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;

namespace TodoApiMPP.Mappings

{
    public class ProductShopMappings : Profile
    {
        public ProductShopMappings()
        {
            CreateMap<ProductShopDTO, ProductShop>();
        }
    }
}