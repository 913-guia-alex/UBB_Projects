// lib/main.dart

import 'package:flutter/material.dart';
import 'package:test_app_package/screens/membership_list_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Gym Membership App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home:  GymScreen(),
    );
  }
}
