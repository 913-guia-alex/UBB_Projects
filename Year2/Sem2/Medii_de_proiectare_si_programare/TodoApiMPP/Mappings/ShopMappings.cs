using AutoMapper;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;

namespace TodoApiMPP.Mappings

{
    public class ShopMappings : Profile
    {
        public ShopMappings()
        {
            CreateMap<ShopDTO, Shop>();
        }
    }
}