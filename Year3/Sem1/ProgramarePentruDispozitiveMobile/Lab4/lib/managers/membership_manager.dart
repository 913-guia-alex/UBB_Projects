// lib/managers/membership_manager.dart

import 'package:test_app_package/models/gym_membership.dart';
import 'package:test_app_package/DataBaseProvider/database_provider.dart';


class MembershipManager {
  static final DatabaseProvider _databaseProvider = DatabaseProvider.instance;
  static int? _lastMembershipId; // Make it nullable

  static Future<void> initialize() async {
    _lastMembershipId = await _databaseProvider.getLastMembershipId() ?? 0;
  }

  static Future<void> addMembership(GymMembership membership) async {
    await _databaseProvider.addMembership(membership);
  }

  static Future<List<GymMembership>> getAllMemberships() async {
    return await _databaseProvider.getAllMemberships();
  }

  static Future<void> updateMembership(GymMembership membership) async {
    await _databaseProvider.updateMembership(membership);
  }

  static Future<void> deleteMembership(int id) async {
    await _databaseProvider.deleteMembership(id);
  }

  static int generateNewMembershipId() {
    _lastMembershipId ??= 0;
    _lastMembershipId = _lastMembershipId! + 1;
    return _lastMembershipId!;
  }
}
