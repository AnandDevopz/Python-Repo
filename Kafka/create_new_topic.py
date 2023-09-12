from confluent_kafka.admin import AdminClient, NewTopic

# Define Kafka broker configuration
broker_config = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker(s) address
}

# Create an AdminClient instance
admin_client = AdminClient(broker_config)

# Define the topic name and its configuration
topic_name = 'my_topic'
num_partitions = 3  # Number of partitions for the topic
replication_factor = 1  # Replication factor for the topic

# Create a NewTopic instance
new_topic = NewTopic(topic=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

# Create the topic
admin_client.create_topics([new_topic])

# Close the AdminClient
admin_client.close()

print(f"Topic '{topic_name}' created successfully with {num_partitions} partitions and replication factor {replication_factor}.")
