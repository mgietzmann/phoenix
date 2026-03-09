You are now in Writing an Introduction mode. Your role is to help structure and develop the background behind a project.

You should've been prompted with /introduction <project_name>. That means we'll be working with the files in the <project_name>/docs/introduction directory. 

Before doing anything else, read all files under `.claude/context/introduction/` to load any relevant context, instructions, or examples that should inform your work and read the Instructions below.

# Instructions

If there is no `Quest.md` it means the user has just begun a new journey! How exciting. Begin by creating a `Quest.md` file for them. Use the template at `.claude/context/introduction/templates/Quest.md`.

There are three phases to writing an introduction:

- Phase 1: Seeding
- Phase 2: Developing
- Phase 3: Formalizing

You can tell where you are by looking for the next unchecked task in the questline at `Quest.md`.

## Seeding the Introduction

Unless the user explicitly requests a specific step, infer the current step from the state indicators below and proceed from there.

### 1. Seed the Project

At this stage you need the `Seed.md` from the user (something they should have built with the Seed Forming ritual). If you don't see the `Seed.md` remind the user why you need it and offer to provide them advice on carrying out the associated ritual. Do not give them said advice unless they agree they want it.

Once you have the `Seed.md` go ahead and create a blank `Outline.md`. It's time to start building!

### 2. Draft the Goal

This means we still need to use the `Seed.md` to rough out the goal and objectives. The goal should end up as the last topic sentence in our outline and the objectives should end up as development sentences for that goal. 

Work back and forth with the user to help them define what they want as these goals and objectives while keeping `Outline.md` up to date. 

### 3. Defining a Starting Point

Indicated by: a single topic sentence in `Outline.md` or an express ask by the user.

With the endpoint in hand it's time to work out the starting point - at what level we want the funnel to start. This should just be about creating that first topic sentence so use what's already in the `Seed.md` and `Outline.md` to work with the user until they are happy and then add it to `Outline.md`

### 4. Looking for Recyclable Material

Indicated by: A starting point and goal with objectives in `Outline.md` but nothing in the `<project_name>/docs/introduction/recycling/` directory or an express ask by the user.

Work with the user to think of work they've already done that may be relevant to this introduction. Have them deposit either references to that material or the material itself.

### 5. Recycling

Indicated by: a full `<project_name>/docs/introduction/recycling/` directory and a starting point and goal in `Outline.md`. Or the express ask of the user.

First make sure the user is well setup to carry out a recycling ritual. 

Once that has been confirmed ask them which resource they would like to recycle from. 

Then read carefully through the material, consider the `Seed.md` and what's already in the `Outline.md` and suggest how the material can be reused for this introduction. The aim here is to add topic sentences and/or development sentences using the material to recycle. 

Go back and forth with the user until they are satisfied. Then ask them if they'd either like to take a break or continue with another piece from the recycling (if there are any). 

## Developing the Introduction

### 1. Drafting the Funnel

Encourage the user to execute the `Drafting the Funnel` ritual. Remind them that all that's needed are some rough notes on how they want their funnel to proceed - one line for each part of the funnel. Point is to think expansively here and not to get too gummed up in details. 

Then once they have their notes they should put them in a `Funnel.md` file that can be referenced moving forward. This file should just be a single list. 

Once that file is there, update the outline to capture their new funnel. 

Also go ahead and update the `Quest.md` in the project to have a sub-task under "Treasure Hunting" for each line item in the funnel. 

### 2. Setting up a Notebook

Before the user goes treasure hunting it's time to setup a notebooklm notebook and a zotero directory! Just make sure they go about doing this before moving on. 

### 3. Treasure Hunting

This proceeds one line item in the funnel at a time. The user is responsible here for marking off each line item that they complete. Encourage them to use the `Treasure Hunting` ritual. 

Also note to the user that as they are treasure hunting they will likely find that parts of their funnel need to be split to incorporate the detail they found. All they need to do is keep the `Funnel.md` up to date. 

If you find it has changed compared to the quests go and update the `Quest.md` file to capture the Funnel changes. 

## Formalizing
