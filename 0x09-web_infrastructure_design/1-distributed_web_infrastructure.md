# Distributed Web Infrastructure

![Distributed Web Infrastructure](./diagrams/1-distributed_web_infrastructure.png)

This file describes a distributed web infrastructure with improved scalability and redundancy.

## Infrastructure Components
- **3 servers:**
  - 1 Load balancer (HAProxy).
  - 2 Web/Application servers.
- **Web server:** Nginx.
- **Application server:** Hosts application files.
- **Database:** MySQL with a Primary-Replica setup.
- **Load balancer:** Distributes incoming traffic between servers.

## Key Explanations:
1. **Why add these components?**
   - Load balancer: Ensures high availability and distributes traffic.
   - Multiple servers: Redundancy and fault tolerance.
   - Primary-Replica database: Improves read performance and fault tolerance.

2. **Distribution algorithm of the load balancer:**
   The load balancer uses round-robin, distributing traffic evenly across servers.

3. **Active-Active vs Active-Passive:**
   - **Active-Active:** All servers handle traffic simultaneously.
   - **Active-Passive:** One server handles traffic, the other remains on standby.

4. **How Primary-Replica works:**
   The Primary database handles writes, while replicas handle read operations.

5. **Primary vs Replica node:**
   - Primary: Receives write and update queries.
   - Replica: Synchronizes data from the Primary and handles read operations.

## Issues:
- **SPOF in the load balancer:** If the load balancer fails, traffic cannot be routed.
- **No HTTPS:** Communication is not secure.
- **No monitoring:** Failures or issues might go unnoticed.

