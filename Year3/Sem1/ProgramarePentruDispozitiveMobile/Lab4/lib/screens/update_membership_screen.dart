import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:test_app_package/managers/membership_manager.dart';
import 'package:test_app_package/models/gym_membership.dart';

class UpdateMembershipScreen extends StatefulWidget {
  final GymMembership membership;
  final VoidCallback onUpdate;

  UpdateMembershipScreen({required this.membership, required this.onUpdate});

  @override
  _UpdateMembershipScreenState createState() => _UpdateMembershipScreenState();
}

class _UpdateMembershipScreenState extends State<UpdateMembershipScreen> {
  late TextEditingController firstNameController;
  late TextEditingController lastNameController;
  late TextEditingController emailController;
  late TextEditingController creationDateController;
  late TextEditingController expirationDateController;
  late TextEditingController gymNameController;

  @override
  void initState() {
    super.initState();
    firstNameController = TextEditingController(text: widget.membership.firstName);
    lastNameController = TextEditingController(text: widget.membership.lastName);
    emailController = TextEditingController(text: widget.membership.email);
    creationDateController = TextEditingController(text: widget.membership.creationDate);
    expirationDateController = TextEditingController(text: widget.membership.expirationDate);
    gymNameController = TextEditingController(text: widget.membership.gymName);
  }

  @override
  void dispose() {
    // Ensure that there are no lingering references or resources
    // Tied to the text input fields after the widget is no longer needed.
    firstNameController.dispose();
    lastNameController.dispose();
    emailController.dispose();
    creationDateController.dispose();
    expirationDateController.dispose();
    gymNameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Update Membership'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              TextField(
                controller: firstNameController,
                decoration: InputDecoration(labelText: 'First Name'),
              ),
              TextField(
                controller: lastNameController,
                decoration: InputDecoration(labelText: 'Last Name'),
              ),
              TextField(
                controller: emailController,
                decoration: InputDecoration(labelText: 'Email'),
              ),
              TextField(
                controller: creationDateController,
                decoration: InputDecoration(labelText: 'Creation Date'),
              ),
              TextField(
                controller: expirationDateController,
                decoration: InputDecoration(labelText: 'Expiration Date'),
              ),
              TextField(
                controller: gymNameController,
                decoration: InputDecoration(labelText: 'Gym Name'),
              ),
              SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  // Validate and update membership
                  _updateMembership();
                },
                child: Text('Submit'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showErrorDialog(String errorMessage) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('Error'),
          content: Text(errorMessage),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }


  void _updateMembership() {
    // Perform validation and update membership in the list
    // Removes any leading or trailing whitespace
    final firstName = firstNameController.text.trim();
    final lastName = lastNameController.text.trim();
    final email = emailController.text.trim();
    final creationDate = creationDateController.text.trim();
    final expirationDate = expirationDateController.text.trim();
    final gymName = gymNameController.text.trim();


    // Validation for name (only alphabetic letters)
    final namePattern = RegExp("^[a-zA-Z ]+\$");
    if (!namePattern.hasMatch(firstName) || !namePattern.hasMatch(lastName)) {
      _showErrorDialog('Invalid name. Please use only alphabetic letters.');
      return;
    }

    // Validation for email
    final emailPattern = RegExp(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$");
    if (!emailPattern.hasMatch(email)) {
      _showErrorDialog('Invalid email format.');
      return;
    }

    // Validation for date format (creation and expiration dates)
    final dateFormat = DateFormat("yyyy-MM-dd");
    try {
      dateFormat.parse(creationDate);
      dateFormat.parse(expirationDate);
    } catch (e) {
      _showErrorDialog('Invalid date format. Please use yyyy-MM-dd.');
      return;
    }

    if (firstName.isNotEmpty && lastName.isNotEmpty && email.isNotEmpty && creationDate.isNotEmpty && expirationDate.isNotEmpty && gymName.isNotEmpty) {
      final updatedMembership = widget.membership.copyWith(
        firstName: firstName,
        lastName: lastName,
        email: email,
        creationDate: creationDate,
        expirationDate: expirationDate,
        gymName: gymName,
      );

      MembershipManager.updateMembership(updatedMembership);

      // Notify the parent screen about the update
      widget.onUpdate();

      // Navigate back to the membership list screen
      Navigator.pop(context);
    } else {
      // Display an error message or handle invalid input
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Error'),
            content: Text('Please fill in all required fields.'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: Text('OK'),
              ),
            ],
          );
        },
      );
    }
  }
}
