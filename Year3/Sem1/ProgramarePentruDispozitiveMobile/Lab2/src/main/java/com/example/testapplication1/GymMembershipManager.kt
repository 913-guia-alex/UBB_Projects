package com.example.testapplication1

private var lastMembershipId = 0


object GymMembershipManager {
    private val memberships = mutableListOf<GymMembership>()


    fun getAllMemberships(): List<GymMembership> {
        return memberships.toList()
    }

    fun generateNewMembershipId(): Int {
        return lastMembershipId++
    }

    fun addMembership(newMembership: GymMembership) {
        memberships.add(newMembership)
    }

    fun deleteMembership(membershipId: Int) {
        val membership = memberships.find { it.id == membershipId }
        membership?.let { memberships.remove(it) }
    }

    fun updateMembership(updatedMembership: GymMembership) {
        val index = memberships.indexOfFirst { it.id == updatedMembership.id }

        if (index != -1) {
            memberships[index].firstName = updatedMembership.firstName
            memberships[index].lastName = updatedMembership.lastName
            memberships[index].email = updatedMembership.email
            memberships[index].creationDate = updatedMembership.creationDate
            memberships[index].expirationDate = updatedMembership.expirationDate
            memberships[index].gymName = updatedMembership.gymName
        }
    }
}
