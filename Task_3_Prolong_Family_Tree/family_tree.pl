% ============================================================
% Task 3: Prolog Family Tree
% ============================================================
% This program defines family relationships including:
% grandparents, parents, children, grandchildren, cousins,
% uncles and aunts.
% ============================================================

% ----------------------------
% Gender facts
% ----------------------------

male(john).
male(peter).
male(mark).
male(david).
male(kevin).
male(brian).

female(mary).
female(susan).
female(ann).
female(jane).
female(lucy).
female(grace).
female(rita).

% ----------------------------
% Parent facts
% parent(Parent, Child).
% ----------------------------

parent(john, mary).
parent(susan, mary).

parent(john, peter).
parent(susan, peter).

parent(mary, ann).
parent(mark, ann).

parent(mary, kevin).
parent(mark, kevin).

parent(peter, jane).
parent(lucy, jane).

parent(peter, brian).
parent(lucy, brian).

parent(ann, grace).
parent(david, grace).

parent(jane, rita).
parent(kevin, rita).

% ----------------------------
% Relationship rules
% ----------------------------

father(X, Y) :-
    % X is the father if X is a male parent of Y.
    parent(X, Y),
    male(X).

mother(X, Y) :-
    % X is the mother if X is a female parent of Y.
    parent(X, Y),
    female(X).

child(X, Y) :-
    % X is a child of Y if Y is a parent of X.
    parent(Y, X).

son(X, Y) :-
    % A son is a male child.
    child(X, Y),
    male(X).

daughter(X, Y) :-
    % A daughter is a female child.
    child(X, Y),
    female(X).

grandparent(X, Y) :-
    % X is a grandparent if X is a parent of Y's parent.
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    % A grandfather is a male grandparent.
    grandparent(X, Y),
    male(X).

grandmother(X, Y) :-
    % A grandmother is a female grandparent.
    grandparent(X, Y),
    female(X).

grandchild(X, Y) :-
    % X is a grandchild of Y if Y is a grandparent of X.
    grandparent(Y, X).

sibling(X, Y) :-
    % Siblings share a parent but are not the same person.
    parent(Z, X),
    parent(Z, Y),
    X \= Y,
    \+ (
        parent(OtherParent, X),
        parent(OtherParent, Y),
        OtherParent @< Z
    ).

brother(X, Y) :-
    % A brother is a male sibling.
    sibling(X, Y),
    male(X).

sister(X, Y) :-
    % A sister is a female sibling.
    sibling(X, Y),
    female(X).

uncle(X, Y) :-
    % An uncle is a brother of someone's parent.
    brother(X, Z),
    parent(Z, Y).

aunt(X, Y) :-
    % An aunt is a sister of someone's parent.
    sister(X, Z),
    parent(Z, Y).

cousin(X, Y) :-
    % Cousins have parents who are siblings.
    parent(A, X),
    parent(B, Y),
    sibling(A, B),
    X \= Y.
