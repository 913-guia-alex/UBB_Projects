// app_bar.dart
import 'package:flutter/material.dart';
import 'package:test_app_package/screens/add_membership_screen.dart';


AppBar buildAppBar(BuildContext context, Function updateMemberships) {
  return AppBar(
    title: Text('Gym Memberships'),
    actions: [
      IconButton(
        icon: Icon(Icons.add),
        onPressed: () {
          // Navigate to the AddMembershipScreen
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => AddMembershipScreen(
                onMembershipAdded: updateMemberships(),
              ),
            ),
          );
        },
      ),
    ],
  );
}
