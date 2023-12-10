// membership_card.dart
import 'package:flutter/material.dart';

Card buildMembershipCard({
  required String firstName,
  required String lastName,
  required String id,
  required String email,
  required String creationDate,
  required String expirationDate,
  required String gymName,

  required Function onUpdate,
  required Function onDelete,
}) {
  return Card(
    elevation: 4.0,
    margin: EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(16.0), // Adjust the radius as needed
    ),
    child: ClipRRect(
      borderRadius: BorderRadius.circular(16.0),
      child: ListTile(
        title: Text('$firstName $lastName'),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('ID: $id'),
            Text('Email: $email'),
            // Add other details as needed
          ],
        ),
        trailing: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            IconButton(
              icon: Icon(Icons.edit),
              onPressed: onUpdate(),
            ),
            IconButton(
              icon: Icon(Icons.delete),
              onPressed: onDelete(),
            ),
          ],
        ),
      ),
    ),
  );
}
