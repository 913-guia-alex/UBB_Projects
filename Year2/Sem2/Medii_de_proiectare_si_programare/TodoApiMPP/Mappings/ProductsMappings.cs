using AutoMapper;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;

namespace TodoApiMPP.Mappings

{
    public class ProductsMappings : Profile
    {
        public ProductsMappings()
        {
            CreateMap<ProductsDTO, Products>();
        }
    }
}