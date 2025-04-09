# 🚨 Postmortem: “The Curious Case of the Vanishing Homepage”  
### Outage Date: March 28, 2025  
### Duration: 1 hour 47 minutes (From 3:12 PM to 5:00 PM WAT)

---

## 📝 Issue Summary

On March 28th, 2025, from 3:12 PM to 5:00 PM (WAT), our production web service **Homeify** (a fictional property listing website) experienced a critical outage where the homepage failed to load for **84% of users**. Users reported an endless loading screen or a generic 502 Bad Gateway error. The root cause was traced to a misconfigured **Nginx server update**, which caused upstream timeout failures.

---

## 🕒 Timeline

- **3:12 PM** – Monitoring alerts triggered high 502 error rates from the load balancer.  
- **3:13 PM** – Engineer on-call verified homepage down from multiple regions.  
- **3:15 PM** – Assumed backend API was unresponsive; restarted backend servers.  
- **3:30 PM** – No effect; restarted Redis and PostgreSQL just in case (it wasn’t them).  
- **3:45 PM** – Escalated to DevOps team after frontend+backend debugging dead-ends.  
- **4:00 PM** – DevOps discovered `/etc/nginx/nginx.conf` was recently patched manually during a routine security update without a restart.  
- **4:10 PM** – Nginx restarted properly, but misconfigured `proxy_read_timeout` setting was causing upstream API failures.  
- **4:45 PM** – Correct `proxy_read_timeout` value set and config reloaded.  
- **5:00 PM** – All systems back online. Incident closed.

---

## 🔍 Root Cause and Resolution

**Root Cause:**  
The outage stemmed from a misconfigured Nginx setting during a manual security patch. The `proxy_read_timeout` was set to an extremely low value (`1s` instead of `60s`), causing Nginx to drop connections to the backend before it could return responses. This change was not tested in staging nor documented in the deployment notes.

**Resolution:**  
The DevOps team identified the config error and updated `proxy_read_timeout` to `60s`, followed by a safe `nginx -s reload`. Monitoring metrics normalized immediately, and page load success rates returned to 99.9%.

---

## 🔧 Corrective and Preventative Measures

### What can be improved:
- More rigorous config change review and automated testing.  
- Improved staging-to-production deployment workflow.  
- Better communication between frontend/backend and DevOps.

### ✅ TODOs:
- [ ] Patch all staging servers with same config and validate changes before production.  
- [ ] Implement automated Nginx config syntax & health tests in CI/CD pipeline.  
- [ ] Add alerting on Nginx 502/504 error thresholds.  
- [ ] Document and enforce a configuration change protocol.  
- [ ] Educate team on proper timeout settings with real-world examples.

---

## 😂 Humor Break: A Diagram of What Happened

USER ----> NGINX ----> (times out) ----> BACKEND 🙃 "No response in 1s? I'm OUT." 💥

Moral of the story? Don’t let your load balancer develop trust issues.

---

## 📚 Repo Info

GitHub repository: alx-system_engineering-devops  
Directory: 0x19-postmortem  
File: README.md
