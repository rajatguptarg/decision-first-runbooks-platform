# Product Overview

## Decision First Runbook App

A production-ready reference implementation for managing and displaying decision-first incident runbooks. The application enables teams to author, store, and execute structured incident response procedures through an interactive viewer and editor interface.

### What a "Decision First Runbook" could mean

**Runbook basics:** A runbook is a detailed set of instructions for handling operational tasks or incidents. It gives step-by-step guidance so that anyone can perform the task consistently.

**Decision-first approach:** Instead of being purely procedural, a decision-first runbook likely emphasizes decision points. This means the document doesn’t just tell you what to do, it starts by clarifying what decision needs to be made, what data or signals inform that decision, and only then outlines actions to take depending on the outcome.

**Use case:** In incident response, for example, a decision-first runbook might begin with “Decide if this outage is customer-impacting or internal only.” Then, based on that decision, it branches into different workflows.

### Why teams use it

- To avoid blindly following steps and instead ensure responders think critically about the situation.
- To make sure ownership and escalation paths are aligned with key decisions, not just tasks.
- To shorten resolution times by clarifying the first choice that changes the response path.

## Core Purpose

Build a small but complete app to author, store, and run decision-first incident runbooks with a fast viewer and a simple editor. The system supports role-based access control, session tracking, and export capabilities to facilitate effective incident management.

## Key Features

- **CRUD Operations**: Create, read, update, and delete runbooks and decision trees
- **Interactive Viewer**: Read-only viewer that mirrors canvas demo functionality
- **Session Management**: Timeline tracking of user actions per incident session
- **Search & Filter**: Search by title, owner, or severity level
- **Export Capabilities**: JSON export of runbooks and current node path
- **Print Support**: Print-friendly view for offline reference
- **Role-Based Access**: Viewer and editor roles with appropriate permissions

## Target Users

- **Incident Responders**: Navigate through structured runbook procedures during incidents
- **Editors**: Create and maintain up-to-date incident response procedures
- **System Administrators**: Manage user roles and system configuration

## Business Value

- Standardizes incident response procedures across teams
- Reduces mean time to resolution through structured decision trees
- Provides audit trails of incident response actions
- Enables knowledge sharing and procedure documentation