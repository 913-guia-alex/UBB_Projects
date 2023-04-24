using AutoMapper;
using TodoApiMPP.Models;
using TodoApiMPP.DTO;

namespace TodoApiMPP.Mappings

{
    public class CoachMappings : Profile
    {
        public CoachMappings()
        {
            CreateMap<CoachDTO, Coach>();
            CreateMap<Coach, CoachDTO>();
            CreateMap<AddCoachDTO, Coach>();
        }
    }
}