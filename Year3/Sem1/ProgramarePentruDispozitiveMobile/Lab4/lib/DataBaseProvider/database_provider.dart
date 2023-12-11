import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';
import 'package:logger/logger.dart';
import 'package:test_app_package/models/gym_membership.dart';

class DatabaseProvider {
  static const _databaseName = 'gym_database.db';
  static const _databaseVersion = 1;

  DatabaseProvider._();
  static final DatabaseProvider instance = DatabaseProvider._();

  static Database? _database;
  final Logger _logger = Logger(); // Create a logger instance

  Future<Database> get database async {
    if (_database != null) return _database!;

    _database = await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    final path = join(await getDatabasesPath(), _databaseName);

    return await openDatabase(
      path,
      version: _databaseVersion,
      onCreate: _createDatabase,
    );
  }

  Future<void> _createDatabase(Database db, int version) async {
    await db.execute('''
      CREATE TABLE gym_memberships(
        id INTEGER PRIMARY KEY,
        firstName TEXT,
        lastName TEXT,
        email TEXT,
        creationDate TEXT,
        expirationDate TEXT,
        gymName TEXT
      )
    ''');
  }

  Future<void> addMembership(GymMembership membership) async {
    try {
      final db = await database;
      await db.insert('gym_memberships', membership.toMap(),
          conflictAlgorithm: ConflictAlgorithm.replace);
    } catch (e, stackTrace) {
      _logger.e('Error adding membership: $e', error: e, stackTrace: stackTrace);
    }
  }

  Future<List<GymMembership>> getAllMemberships() async {
    try {
      final db = await database;
      final List<Map<String, dynamic>> maps = await db.query('gym_memberships');

      return List.generate(maps.length, (index) {
        return GymMembership.fromMap(maps[index]);
      });
    } catch (e, stackTrace) {
      _logger.e('Error getting all memberships: $e', error: e, stackTrace: stackTrace);
      return [];
    }
  }

  Future<void> updateMembership(GymMembership membership) async {
    try {
      final db = await database;
      await db.update(
        'gym_memberships',
        membership.toMap(),
        where: 'id = ?',
        whereArgs: [membership.id],
      );
    } catch (e, stackTrace) {
      _logger.e('Error updating membership: $e', error: e, stackTrace: stackTrace);}
  }

  Future<void> deleteMembership(int id) async {
    try {
      final db = await database;
      await db.delete(
        'gym_memberships',
        where: 'id = ?',
        whereArgs: [id],
      );
    } catch (e, stackTrace) {
      _logger.e('Error deleting membership: $e', error: e, stackTrace: stackTrace);
    }
  }

  Future<int?> getLastMembershipId() async {
    try {
      final db = await database;
      final result =
      await db.rawQuery('SELECT MAX(id) as last_id FROM gym_memberships');
      final lastId = result.first['last_id'];
      return lastId as int?;
    } catch (e, stackTrace) {
      _logger.e('Error getting last membership ID: $e', error: e, stackTrace: stackTrace);
      return null;
    }
  }
}
