'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { 
  User, Target, Briefcase, MapPin, Award, Zap, Heart, 
  Camera, Clock, Github, Linkedin, Globe, Settings, 
  Save, X, Plus, Sparkles, ShieldCheck, Loader2, Building2
} from 'lucide-react';
import { Navigation } from '@/components/Navigation';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { cn } from '@/lib/utils';

export default function ProfilePage() {
  const router = useRouter();
  const [mounted, setMounted] = useState(false);
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  
  // États pour les données
  const [profile, setProfile] = useState<any>(null);
  const [editData, setEditData] = useState<any>(null);
  const [session, setSession] = useState<any>(null);

  useEffect(() => {
    setMounted(true);
    const storedUser = localStorage.getItem('user');
    const token = localStorage.getItem('token');
    
    if (storedUser && token) {
      const user = JSON.parse(storedUser);
      setSession(user);
      fetchProfile(user.id, token);
    } else {
      router.push('/auth/login');
    }
  }, [router]);

  const fetchProfile = async (userId: string, token: string) => {
    try {
      const res = await fetch(`http://localhost:8000/api/auth/profile/${userId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        const cleanData = {
          ...data,
          competences: data.competences || [],
          env_travail_prefere: data.env_travail_prefere || [],
          points_de_douleur: data.points_de_douleur || [],
          centres_interet: data.centres_interet || [],
          langues: data.langues || []
        };
        setProfile(cleanData);
        // Initialisation propre pour éviter les warnings "uncontrolled to controlled"
        setEditData({
          nom: '',
          prenom: '',
          age: 0,
          ville: '',
          statut: '',
          domaine_activite: '',
          poste_actuel: '',
          nom_entreprise: '',
          bio: '',
          linkedin_url: '',
          github_url: '',
          site_web: '',
          recherche_active: false,
          annees_experience: 0,
          ...cleanData
        });
      }
    } catch (err) {
      console.error("Erreur de récupération profil", err);
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async () => {
    setIsSaving(true);
    try {
      const token = localStorage.getItem('token');
      const res = await fetch(`http://localhost:8000/api/auth/profile/update/${session.id}`, {
        method: 'PUT',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(editData)
      });

      if (res.ok) {
        setProfile(editData);
        setIsEditing(false);
      }
    } catch (err) {
      console.error("Erreur de sauvegarde", err);
    } finally {
      setIsSaving(false);
    }
  };

  // --- LOGIQUE GESTION TAGS (Édition) ---
  const handleAddTag = (field: string, value: string) => {
    if (!value.trim()) return;
    setEditData({ ...editData, [field]: [...(editData[field] || []), value.trim()] });
  };

  const handleRemoveTag = (field: string, value: string) => {
    setEditData({ ...editData, [field]: editData[field].filter((t: string) => t !== value) });
  };

  if (!mounted || loading) return <Loader />;

  return (
    <div className="min-h-screen bg-[#050505] text-white selection:bg-primary/30 font-sans overflow-x-hidden">
      <Navigation currentPath="/profile" />

      {/* Arrière-plan Dynamique */}
      <div className="fixed inset-0 -z-10 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-primary/5 via-transparent to-transparent opacity-50" />
      <div className="fixed top-[-20%] left-[-10%] w-[60%] h-[60%] bg-primary/10 rounded-full blur-[120px] animate-pulse" />

      <main className="max-w-6xl mx-auto w-full px-4 pt-12 pb-32 space-y-10 animate-in fade-in slide-in-from-bottom-5 duration-1000">
        
        {/* HEADER HERO : LE HUB D'IDENTITÉ */}
        <Card className="relative overflow-hidden border-white/5 bg-white/[0.03] backdrop-blur-3xl rounded-[3.5rem] p-10 md:p-14 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.5)]">
          <div className="flex flex-col md:flex-row items-center md:items-start gap-12 z-10 relative">
            
            {/* Avatar Premium avec lueur */}
            <div className="relative group">
              <div className="absolute -inset-1 bg-gradient-to-r from-primary to-accent rounded-full blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
              <div className="relative w-36 h-36 md:w-48 md:h-48 rounded-full bg-black p-1">
                <div className="w-full h-full rounded-full bg-gradient-to-br from-[#111] to-[#050505] flex items-center justify-center text-6xl font-black text-transparent bg-clip-text bg-gradient-to-br from-primary to-accent">
                  {profile.prenom?.[0] || session.name?.[0]}
                </div>
              </div>
              {isEditing && (
                <button className="absolute bottom-2 right-2 bg-primary p-3 rounded-full shadow-xl hover:scale-110 active:scale-95 transition-all">
                  <Camera className="w-5 h-5" />
                </button>
              )}
            </div>

            {/* Infos Identité */}
            <div className="flex-1 text-center md:text-left space-y-6">
              <div className="space-y-4">
                {isEditing ? (
                  <div className="flex flex-col md:flex-row gap-4">
                    <EditInput value={editData?.prenom ?? ''} onChange={(v: string) => setEditData({...editData, prenom: v})} placeholder="Prénom" className="text-2xl font-bold" />
                    <EditInput value={editData?.nom ?? ''} onChange={(v: string) => setEditData({...editData, nom: v})} placeholder="Nom" className="text-2xl font-bold" />
                  </div>
                ) : (
                  <h1 className="text-5xl md:text-7xl font-black tracking-tighter leading-none bg-clip-text text-transparent bg-gradient-to-b from-white to-white/60">
                    {profile.prenom} {profile.nom}
                  </h1>
                )}
                
                <div className="flex items-center justify-center md:justify-start gap-4">
                   <div className="flex flex-col md:flex-row items-center gap-4">
                    <div className="flex items-center gap-2 px-4 py-2 bg-white/5 border border-white/10 rounded-2xl text-sm font-bold text-muted-foreground">
                      <Briefcase className="w-4 h-4 text-primary" />
                      {isEditing ? (
                        <input className="bg-transparent border-none focus:ring-0 w-32 outline-none" placeholder="Poste" value={editData.poste_actuel ?? ''} onChange={e => setEditData({...editData, poste_actuel: e.target.value})} />
                      ) : profile.poste_actuel || "Poste non défini"}
                    </div>

                    <div className="flex items-center gap-2 px-4 py-2 bg-white/5 border border-white/10 rounded-2xl text-sm font-bold text-muted-foreground">
                      <Building2 className="w-4 h-4 text-accent" />
                      {isEditing ? (
                        <input className="bg-transparent border-none focus:ring-0 w-32 outline-none" placeholder="Entreprise" value={editData.nom_entreprise ?? ''} onChange={e => setEditData({...editData, nom_entreprise: e.target.value})} />
                      ) : profile.nom_entreprise || "Structure non définie"}
                    </div>

                    <div className="flex items-center gap-2 px-4 py-2 bg-white/5 border border-white/10 rounded-2xl text-sm font-bold text-muted-foreground">
                      <MapPin className="w-4 h-4 text-primary" />
                      {isEditing ? (
                        <input className="bg-transparent border-none focus:ring-0 w-24 outline-none" placeholder="Ville" value={editData.ville ?? ''} onChange={e => setEditData({...editData, ville: e.target.value})} />
                      ) : profile.ville || "Ville non définie"}
                    </div>
                   </div>
                   
                   {/* Années d'expérience */}
                   <div className="flex items-center gap-2 px-4 py-2 bg-white/5 border border-white/10 rounded-2xl text-sm font-bold text-muted-foreground">
                      <Zap className="w-4 h-4 text-yellow-400" />
                      {isEditing ? (
                        <input type="number" className="bg-transparent border-none focus:ring-0 w-20 outline-none" placeholder="Ans" value={editData.annees_experience ?? 0} onChange={e => setEditData({...editData, annees_experience: parseInt(e.target.value) || 0})} />
                      ) : (profile.annees_experience || 0) + " ans d'exp."}
                    </div>

                    {/* Social Links Fast Access */}
                    {!isEditing && (
                      <div className="flex items-center gap-3 ml-2">
                        {profile.linkedin_url && <a href={profile.linkedin_url} target="_blank" className="hover:text-primary transition-colors"><Linkedin className="w-5 h-5" /></a>}
                        {profile.github_url && <a href={profile.github_url} target="_blank" className="hover:text-primary transition-colors"><Github className="w-5 h-5" /></a>}
                        {profile.site_web && <a href={profile.site_web} target="_blank" className="hover:text-primary transition-colors"><Globe className="w-5 h-5" /></a>}
                      </div>
                    )}
                </div>
              </div>

              {/* Badges & Stats */}
              <div className="flex flex-wrap items-center justify-center md:justify-start gap-3">
                <Badge variant="secondary" className="bg-primary/10 text-primary border-primary/20 hover:bg-primary/20 px-4 py-1.5 rounded-full font-black text-[10px] tracking-widest uppercase">
                  ADN PROFESSIONNEL {profile.is_onboarding_complete ? 'VÉRIFIÉ' : 'À COMPLÉTER'}
                </Badge>
                {profile.recherche_active && (
                  <Badge className="bg-green-500/10 text-green-400 border-green-500/20 px-4 py-1.5 rounded-full font-black text-[10px] tracking-widest uppercase">
                    EN RECHERCHE ACTIVE
                  </Badge>
                )}
                <div className="h-1 w-1 bg-white/20 rounded-full" />
                <span className="text-xs font-bold text-white/40">{profile.views_count || 0} vues sur le profil</span>
              </div>
            </div>

            {/* Boutons d'action */}
            <div className="flex flex-col gap-3">
              {isEditing ? (
                <>
                  <Button onClick={handleSave} disabled={isSaving} className="rounded-2xl px-8 h-14 bg-primary hover:bg-primary/90 font-black gap-3 shadow-[0_10px_30px_-10px_rgba(var(--primary),0.5)] transition-all">
                    {isSaving ? <Loader2 className="w-5 h-5 animate-spin" /> : <Save className="w-5 h-5" />}
                    SAUVEGARDER
                  </Button>
                  <Button onClick={() => { setIsEditing(false); setEditData(profile); }} variant="outline" className="rounded-2xl h-14 border-white/10 hover:bg-white/5 font-bold gap-3">
                    <X className="w-5 h-5" /> ANNULER
                  </Button>
                </>
              ) : (
                <Button onClick={() => setIsEditing(true)} className="rounded-2xl px-8 h-14 bg-white text-black hover:bg-white/90 font-black gap-3 transition-transform active:scale-95 shadow-2xl">
                  <Settings className="w-5 h-5" /> MODIFIER PROFIL
                </Button>
              )}
            </div>
          </div>
        </Card>

        {/* SECTION GRILLE DE CONTENU */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          
          {/* COLONNE GAUCHE : BIO & PARCOURS */}
          <div className="lg:col-span-8 space-y-10">
            
            {/* CARD BIO */}
            <Card className="p-10 rounded-[3rem] bg-white/[0.02] border-white/5 backdrop-blur-md relative overflow-hidden group">
              <div className="absolute top-0 right-0 p-10 opacity-[0.02] transform translate-x-10 translate-y--10 group-hover:scale-110 transition-transform duration-700">
                <Sparkles className="w-64 h-64" />
              </div>
                <div className="flex items-center gap-4 mb-8">
                  <div className="p-3 bg-primary/10 rounded-2xl"><Target className="w-6 h-6 text-primary" /></div>
                  <h3 className="text-2xl font-black tracking-tight">Mon ADN en quelques mots</h3>
                  
                  {isEditing && (
                    <div className="ml-auto flex items-center gap-2">
                       <label className="text-[10px] font-bold text-white/40 uppercase">Recherche Active</label>
                       <input type="checkbox" checked={editData.recherche_active} onChange={e => setEditData({...editData, recherche_active: e.target.checked})} className="w-5 h-5 rounded border-white/10 bg-white/5 accent-primary" />
                    </div>
                  )}
                </div>
                {isEditing ? (
                  <div className="space-y-6">
                    <Textarea 
                      value={editData.bio ?? ''} 
                      onChange={e => setEditData({...editData, bio: e.target.value})} 
                      className="bg-white/5 border-white/10 rounded-3xl min-h-[120px] text-lg p-6 focus:border-primary transition-all"
                      placeholder="Raconte ton histoire..."
                    />
                    
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                      <EditInput value={editData.linkedin_url ?? ''} onChange={(v: string) => setEditData({...editData, linkedin_url: v})} placeholder="LinkedIn URL" className="text-xs h-10" />
                      <EditInput value={editData.github_url ?? ''} onChange={(v: string) => setEditData({...editData, github_url: v})} placeholder="GitHub URL" className="text-xs h-10" />
                      <EditInput value={editData.site_web ?? ''} onChange={(v: string) => setEditData({...editData, site_web: v})} placeholder="Site Web" className="text-xs h-10" />
                    </div>
                  </div>
                ) : (
                <p className="text-xl leading-relaxed text-white/70 italic font-medium">
                  "{profile.bio || "Aucune biographie n'a été ajoutée pour le moment. Cliquez sur modifier pour raconter votre histoire !"}"
                </p>
              )}
            </Card>

            {/* CARD PARCOURS */}
            <Card className="p-10 rounded-[3rem] bg-white/[0.02] border-white/5 backdrop-blur-md">
              <div className="flex items-center gap-4 mb-10">
                <div className="p-3 bg-accent/10 rounded-2xl"><Award className="w-6 h-6 text-accent" /></div>
                <h3 className="text-2xl font-black tracking-tight">Expériences & Parcours</h3>
              </div>
              
              <div className="space-y-10">
                {(isEditing ? editData : profile).parcours_pro?.map((p: any, i: number) => (
                  <div key={i} className="relative pl-10 border-l-2 border-white/5 group hover:border-primary/30 transition-colors">
                    <div className="absolute top-0 left-[-7px] w-3 h-3 rounded-full bg-white/10 group-hover:bg-primary group-hover:shadow-[0_0_15px_rgba(var(--primary),0.5)] transition-all" />
                    <div className="space-y-2">
                       <h4 className="text-lg font-black">{p.type}</h4>
                       <p className="text-white/50 font-medium">{p.detail}</p>
                    </div>
                  </div>
                )) || <div className="text-center py-10 text-white/20 font-bold uppercase tracking-widest">Aucune expérience renseignée</div>}
                
                {isEditing && (
                   <Button variant="ghost" className="w-full h-16 border-2 border-dashed border-white/5 rounded-3xl hover:border-primary/20 hover:bg-primary/5 text-white/30 hover:text-primary font-bold gap-3 transition-all">
                     <Plus className="w-5 h-5" /> Ajouter une expérience
                   </Button>
                )}
              </div>
            </Card>
          </div>

          {/* COLONNE DROITE : SKILLS & PRÉFÉRENCES */}
          <div className="lg:col-span-4 space-y-10">
            
            {/* SKILLS */}
            <Card className="p-8 rounded-[3rem] bg-white/[0.02] border-white/5 backdrop-blur-md">
               <div className="flex items-center gap-3 mb-8">
                <Zap className="w-5 h-5 text-yellow-400" />
                <h3 className="text-lg font-black uppercase tracking-tighter">Hard Skills</h3>
              </div>
              <div className="flex flex-wrap gap-2.5">
                {(isEditing ? editData.competences : profile.competences)?.map((skill: string) => (
                  <Badge key={skill} className="bg-white/5 text-white/80 border-white/10 px-4 py-2 rounded-2xl text-[11px] font-bold group">
                    {skill}
                    {isEditing && <X className="w-3.5 h-3.5 ml-2 cursor-pointer text-white/20 hover:text-red-500" onClick={() => handleRemoveTag('competences', skill)} />}
                  </Badge>
                ))}
                {isEditing && <AddTagInput onAdd={v => handleAddTag('competences', v)} />}
              </div>
            </Card>

            {/* DNA (LIKES/DISLIKES) */}
            <Card className="p-8 rounded-[3rem] bg-white/[0.02] border-white/5 backdrop-blur-md">
              <div className="flex items-center gap-3 mb-8">
                <Heart className="w-5 h-5 text-rose-500" />
                <h3 className="text-lg font-black uppercase tracking-tighter">Mon ADN de Travail</h3>
              </div>
              
              <div className="space-y-10">
                <DnaSection 
                  label="Adore" 
                  items={(isEditing ? editData.env_travail_prefere : profile.env_travail_prefere)} 
                  color="text-primary" 
                  isEditing={isEditing}
                  onAdd={(v: string) => handleAddTag('env_travail_prefere', v)}
                  onRemove={(v: string) => handleRemoveTag('env_travail_prefere', v)}
                />
                <DnaSection 
                  label="Évite" 
                  items={(isEditing ? editData.points_de_douleur : profile.points_de_douleur)} 
                  color="text-rose-500" 
                  isEditing={isEditing}
                  onAdd={(v: string) => handleAddTag('points_de_douleur', v)}
                  onRemove={(v: string) => handleRemoveTag('points_de_douleur', v)}
                />
              </div>
            </Card>

            {/* SECURITE */}
            <div className="p-8 rounded-[2.5rem] bg-gradient-to-br from-white/[0.03] to-transparent border border-white/5 text-center space-y-4">
              <ShieldCheck className="w-8 h-8 text-primary mx-auto opacity-50" />
              <p className="text-[10px] font-black uppercase tracking-[0.3em] text-white/30">Données sécurisées</p>
              <p className="text-xs text-white/40 leading-relaxed font-medium">Votre profil est synchronisé en temps réel avec Supabase PostgreSQL.</p>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
}

// --- SOUS-COMPOSANTS POUR LE "WOW" FACTOR ---

const Loader = () => (
  <div className="min-h-screen bg-black flex flex-col items-center justify-center gap-6">
    <div className="relative">
      <div className="w-20 h-20 border-2 border-primary/20 rounded-full" />
      <div className="absolute inset-0 w-20 h-20 border-2 border-primary border-t-transparent rounded-full animate-spin" />
    </div>
    <span className="text-[10px] font-black uppercase tracking-[0.5em] text-primary animate-pulse">Chargement de votre ADN</span>
  </div>
);

const EditInput = ({ value, onChange, placeholder, className }: any) => (
  <input 
    className={cn("bg-white/5 border border-white/10 rounded-2xl px-6 h-14 outline-none focus:border-primary transition-all text-white w-full", className)}
    value={value ?? ''}
    placeholder={placeholder}
    onChange={e => onChange(e.target.value)}
  />
);

const AddTagInput = ({ onAdd }: { onAdd: (v: string) => void }) => {
  const [v, setV] = useState('');
  return (
    <div className="flex gap-2 w-full mt-2">
      <input 
        className="flex-1 bg-white/5 border border-white/5 rounded-xl px-4 text-xs outline-none focus:border-primary"
        placeholder="Ajouter..."
        value={v}
        onChange={e => setV(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && (onAdd(v), setV(''))}
      />
      <Button onClick={() => (onAdd(v), setV(''))} size="icon" className="w-8 h-8 rounded-xl"><Plus className="w-4 h-4" /></Button>
    </div>
  );
};

const DnaSection = ({ label, items, color, isEditing, onAdd, onRemove }: any) => (
  <div className="space-y-4">
    <p className="text-[10px] font-black uppercase tracking-widest text-white/30">{label}</p>
    <div className="flex flex-wrap gap-2">
      {items?.map((t: string) => (
        <span key={t} className={cn("text-[10px] font-bold px-3 py-1.5 rounded-xl border transition-all", color, `bg-${color}/5`, `border-${color}/20`)}>
          {t}
          {isEditing && <X className="inline-block w-3 h-3 ml-2 cursor-pointer opacity-30 hover:opacity-100" onClick={() => onRemove(t)} />}
        </span>
      ))}
      {!items?.length && !isEditing && <span className="text-[10px] text-white/10 italic">Non renseigné</span>}
    </div>
    {isEditing && <AddTagInput onAdd={onAdd} />}
  </div>
);