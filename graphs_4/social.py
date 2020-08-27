import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # maps IDs to User objects (lookup table for User Objects given IDs)
        self.users = {}
        # Adjacency list
        # maps user_ids to a list of other users (who are their friends)
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):  # O(n)
            self.add_user(f"User {i+1}")  # name doesn't really matter

        # generate all possible friendships, avoiding duplicates
        possible_friendships = []
        for user_id in self.users:  # O(n) * O(n) = O(n^2)
            # if friendship between user 1 and user 2 already exists
            # don't add friendship between user 2 and user 1
            # to prevent this, only look at friendships for user ids higher than user
            for friend_id in range(user_id+1, len(self.users.keys())+1):  # O(n/2) ~ O(n)
                possible_friendships.append((user_id, friend_id))

        # randomly select correct # of friendships
        random.shuffle(possible_friendships)
        # number of friendships = num_users * avg_friendships // 2
        # divide by 2 so we don't count each friendship twice since they are bidirectional
        # (one call to add_friendship adds two friendships)
        num_friendships = num_users * avg_friendships // 2
        # O((n*m)/2) ~ O(n*m); if m = n, actually O(n^2/2) ~ O(n^2)
        for i in range(0, num_friendships):
            user_1, user_2 = possible_friendships[i]
            self.add_friendship(user_1, user_2)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # create a Queue
        queue = Queue()
        # create a set of visited (previously seen) vertices
        # store the friend ID (key): path from user -> friend (value, as a list of user IDs)
        visited = {}  # Note that this is a dictionary, not a set
        # add first user_id to the Queue as a path
        queue.enqueue([user_id])

        # while the queue is not empty:
        while queue.size() > 0:
            # dequeue a current path
            current_path = queue.dequeue()
            # get the current vertex from the end of the path
            current_vertex = current_path[-1]

            if current_vertex not in visited:
                # add vertex to visited
                # also add the PATH that brought us to this vertex
                # key: current vertex, value: path
                visited[current_vertex] = current_path

                # queue up all neighbors as paths
                for neighbor in self.friendships[current_vertex]:
                    # make a new copy of the current path
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    num_users = 5
    average_friendships = 2
    sg.populate_graph(num_users, average_friendships)
    print(sg.friendships)
    user_id = 1
    connections = sg.get_all_social_paths(user_id)
    print(connections)
    print(
        f"Percentage of users in user {user_id}'s social network = {(len(connections)/num_users)*100}%")
    total = 0
    for path in connections.values():
        total += len(path)
    print(f"Avg degree of separation = {total / len(connections) - 1}")
