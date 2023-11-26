// lib/screens/add_membership_screen.dart

import 'package:flutter/material.dart';
import 'package:test_app_package/managers/membership_manager.dart';
import 'package:test_app_package/models/gym_membership.dart';
import 'dart:core';
import 'package:intl/intl.dart';






class AddMembershipScreen extends StatefulWidget {
  final VoidCallback onMembershipAdded;

  const AddMembershipScreen({Key? key, required this.onMembershipAdded}) : super(key: key);

  @override
  _AddMembershipScreenState createState() => _AddMembershipScreenState();
}

class _AddMembershipScreenState extends State<AddMembershipScreen> {
  late TextEditingController firstNameController;
  late TextEditingController lastNameController;
  late TextEditingController emailController;
  late TextEditingController creationDateController;
  late TextEditingController expirationDateController;
  late TextEditingController gymNameController;

  @override
  void initState() {
    super.initState();
    firstNameController = TextEditingController();
    lastNameController = TextEditingController();
    emailController = TextEditingController();
    creationDateController = TextEditingController();
    expirationDateController = TextEditingController();
    gymNameController = TextEditingController();

  }

  @override
  void dispose() {
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
        title: Text('Add Membership'),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
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
                  // Validate and add membership
                  _addMembership();
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


  void _addMembership() {
    // Perform validation and add membership to the list
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
      final newMembership = GymMembership(
        id: MembershipManager.generateNewMembershipId(),
        firstName: firstName,
        lastName: lastName,
        email: email,
        creationDate: creationDate,
        expirationDate: expirationDate,
        gymName: gymName,
      );

      MembershipManager.addMembership(newMembership);

      // Notify the callback that a new membership is added
      widget.onMembershipAdded();

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


