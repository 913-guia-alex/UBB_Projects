using AutoMapper;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;

namespace TodoApiMPP.Mappings

{
    public class ClientMappings : Profile
    {
        public ClientMappings()
        {
            CreateMap<Clients, ClientDTO>();
            CreateMap<ClientDTO, Clients>();
            CreateMap<AddClientDTO, Clients>();
            CreateMap<Coach, CoachDTO>();
            CreateMap<Subscriptions, SubscriptionsDTO>();

        }
    }
}