using AutoMapper;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;

namespace TodoApiMPP.Mappings

{
    public class SubscriptionsMappings : Profile
    {
        public SubscriptionsMappings()
        {
            CreateMap<Subscriptions, SubscriptionsDTO>();
            CreateMap<Clients, ClientDTO>();
        }
    }
}