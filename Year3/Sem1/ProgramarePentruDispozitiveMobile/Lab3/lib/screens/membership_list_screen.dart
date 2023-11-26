// lib/screens/gym_screen.dart

import 'package:flutter/material.dart';
import 'package:test_app_package/managers/membership_manager.dart';
import 'package:test_app_package/models/gym_membership.dart';
import 'package:test_app_package/screens/update_membership_screen.dart';
import 'add_membership_screen.dart';
import 'package:test_app_package/widgets/app_bar.dart';
import 'package:test_app_package/widgets/membership_card.dart';


class GymScreen extends StatefulWidget {
  @override
  _GymScreenState createState() => _GymScreenState();
}

class _GymScreenState extends State<GymScreen> {
  late List<GymMembership> memberships;

  @override
  void initState() {
    super.initState();
    memberships = MembershipManager.getAllMemberships();
  }

  void updateMemberships() {
    setState(() {
      memberships = MembershipManager.getAllMemberships();
    });
  }


  Future<void> _showDeleteConfirmationDialog(int membershipId) async {
    return showDialog<void>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Delete Membership'),
          content: Text('Are you sure you want to delete this membership?'),
          actions: <Widget>[
            TextButton(
              onPressed: () {
                Navigator.of(context).pop(); // Close the dialog
              },
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                // Call deleteMembership function and update the UI
                MembershipManager.deleteMembership(membershipId);
                updateMemberships();
                Navigator.of(context).pop(); // Close the dialog
              },
              child: Text('Yes'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: buildAppBar(context, updateMemberships),
      body: memberships.isEmpty
          ? Center(
        child: Text('No gym memberships available.'),
      )
          : ListView.builder(
        itemCount: memberships.length,
        itemBuilder: (context, index) {
          return MembershipItem(
            membership: memberships[index],
            onUpdate: () {
              _navigateToUpdateScreen(context, memberships[index]);
            },
            onDelete: () {
              _showDeleteConfirmationDialog(memberships[index].id);
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Navigate to the AddMembershipScreen
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => AddMembershipScreen(
                onMembershipAdded: updateMemberships,
              ),
            ),
          );
        },
        child: Text('+'),
      ),
    );
  }



  void _navigateToUpdateScreen(BuildContext context, GymMembership membership) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => UpdateMembershipScreen(
          membership: membership,
          onUpdate: () {
            // Update the UI after the membership is updated
            updateMemberships();
          },
        ),
      ),
    );
  }

}

class MembershipItem extends StatelessWidget {
  final GymMembership membership;
  final VoidCallback onUpdate;
  final VoidCallback onDelete;

  const MembershipItem({
    Key? key,
    required this.membership,
    required this.onUpdate,
    required this.onDelete,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text('${membership.firstName} ${membership.lastName}'),
      subtitle: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('ID: ${membership.id}'),
          Text('Email: ${membership.email}'),
          Text('Creation Date: ${membership.creationDate}'),
          Text('Expiration Date: ${membership.expirationDate}'),
          Text('Gym Name: ${membership.gymName}'),
        ],
      ),
      trailing: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          IconButton(
            icon: Icon(Icons.edit),
            onPressed: onUpdate,
          ),
          IconButton(
            icon: Icon(Icons.delete),
            onPressed: onDelete,
          ),
        ],
      ),
    );
  }


}


