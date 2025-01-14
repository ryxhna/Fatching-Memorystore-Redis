from google.cloud import redis_v1

def get_redis_info(project_id):
    """Fetch Redis instance information for a specific project."""
    client = redis_v1.CloudRedisClient()
    try:
        # Fetch all Redis instances in all locations for the given project
        request = redis_v1.ListInstancesRequest(parent=f"projects/{project_id}/locations/-")
        instances = client.list_instances(request=request)

        # Check if there are no Redis instances
        if not instances.instances: 
            print(f"No Redis instances found for project {project_id}. Skipping...")
            return []

        redis_info = []
        for instance in instances.instances:
            redis_info.append({
                "Project ID": project_id,
                "Instance ID": instance.name.split('/')[-1],
                "Type": instance.tier,
                "Version": instance.redis_version,
                "Location": instance.location_id,
                "Primary Endpoint": f"{instance.host}:{instance.port}",
                "Read Replica": "Yes" if instance.replica_count > 0 else "No",
                "Read Endpoint": f"{instance.read_endpoint}:{instance.read_endpoint_port}" if instance.read_endpoint else "",
                "Instance Capacity (GB)": instance.memory_size_gb,
                "AUTH": "Enabled" if instance.auth_enabled else "Disabled",
                "TLS": "Enabled" if instance.transit_encryption_mode == "SERVER_AUTHENTICATION" else "Disabled",
                "Labels": ", ".join(f"{k}: {v}" for k, v in instance.labels.items()) if instance.labels else "None"
            })
        return redis_info

    except Exception as e:
        print(f"Error fetching Redis instances for project {project_id}: {e}")
        return []
