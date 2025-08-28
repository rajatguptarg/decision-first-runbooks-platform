// MongoDB initialization script
db = db.getSiblingDB('runbooks_db');

// Create collections with validation
db.createCollection('users', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['username', 'email', 'password_hash', 'role', 'created_at'],
      properties: {
        username: { bsonType: 'string' },
        email: { bsonType: 'string' },
        password_hash: { bsonType: 'string' },
        role: { enum: ['admin', 'editor', 'responder'] },
        created_at: { bsonType: 'date' }
      }
    }
  }
});

db.createCollection('runbooks', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['title', 'owner_id', 'severity', 'created_at'],
      properties: {
        title: { bsonType: 'string' },
        description: { bsonType: 'string' },
        owner_id: { bsonType: 'objectId' },
        severity: { enum: ['low', 'medium', 'high', 'critical'] },
        tags: { bsonType: 'array', items: { bsonType: 'string' } },
        created_at: { bsonType: 'date' },
        updated_at: { bsonType: 'date' }
      }
    }
  }
});

db.createCollection('sessions', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['runbook_id', 'user_id', 'status', 'created_at'],
      properties: {
        runbook_id: { bsonType: 'objectId' },
        user_id: { bsonType: 'objectId' },
        status: { enum: ['active', 'paused', 'completed', 'failed'] },
        created_at: { bsonType: 'date' },
        updated_at: { bsonType: 'date' }
      }
    }
  }
});

// Create indexes
db.users.createIndex({ email: 1 }, { unique: true });
db.users.createIndex({ username: 1 }, { unique: true });
db.runbooks.createIndex({ title: 'text', description: 'text' });
db.runbooks.createIndex({ owner_id: 1 });
db.runbooks.createIndex({ severity: 1 });
db.runbooks.createIndex({ tags: 1 });
db.sessions.createIndex({ runbook_id: 1 });
db.sessions.createIndex({ user_id: 1 });
db.sessions.createIndex({ status: 1 });
db.sessions.createIndex({ created_at: -1 });

print('Database initialization completed successfully!');