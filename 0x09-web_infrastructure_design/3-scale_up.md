# Scale Up

![Scale Up](./diagrams/3-scale_up.png)

This file describes scaling up the infrastructure for better performance and reliability.

## Infrastructure Components
- **1 additional server:** Adds capacity for scalability.
- **Load balancer cluster (HAProxy):** Active-Passive setup for redundancy.
- **Separation of concerns:** Web, application, and database servers on separate machines.

## Key Explanations:
1. **Why add these components?**
   - Additional server: Handles more traffic.
   - Load balancer cluster: Prevents downtime if one load balancer fails.
   - Separation of concerns: Improves performance and security.

2. **Active-Passive load balancer:**
   - One load balancer is active, and the other remains on standby, taking over during failure.

3. **Benefits of separation of components:**
   - Improves performance and security by isolating different functions.
