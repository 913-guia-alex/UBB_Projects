// lib/main.dart

import 'package:flutter/material.dart';
import 'package:test_app_package/screens/membership_list_screen.dart';
import 'package:test_app_package/managers/membership_manager.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await MembershipManager.initialize();
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
