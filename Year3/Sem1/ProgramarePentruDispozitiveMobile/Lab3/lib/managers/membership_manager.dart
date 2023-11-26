// lib/managers/membership_manager.dart

import 'package:test_app_package/models/gym_membership.dart';

class MembershipManager {
  static List<GymMembership> memberships = [];
  static int _lastMembershipId = 0;


  static void addMembership(GymMembership newMembership) {
    memberships.add(newMembership);
  }

  static void updateMembership(GymMembership updatedMembership) {
    final index = memberships.indexWhere((member) => member.id == updatedMembership.id);
    if (index != -1) {
      memberships[index] = updatedMembership;
    }
  }

  static void deleteMembership(int membershipId) {
    memberships.removeWhere((membership) => membership.id == membershipId);
  }

  // Function to generate a new auto-incremented membership ID
  static int generateNewMembershipId() {
    _lastMembershipId++;
    return _lastMembershipId;
  }

  static List<GymMembership> getAllMemberships() {
    // Return a copy of the memberships list to avoid direct manipulation
    return List.from(memberships);
  }
}

